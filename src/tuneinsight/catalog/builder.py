"""Utilities to initialize, wait on, and get status of a catalog build."""

import time
from abc import ABC, abstractmethod

import tqdm

from tuneinsight import models
from tuneinsight.api.sdk.api.api_ontology import (
    build_catalog,
    get_build_catalog_progress,
)
from tuneinsight.api.sdk.types import is_set, true_if_unset
from tuneinsight.client import DataSource, Diapason
from tuneinsight.client.validation import validate_response
from tuneinsight.utils.time_tools import render_seconds


class JobProgressTracker(ABC):
    """
    Tracking interface for jobs such as catalog building.

    Classes extending this interface should implement an `update` method
    called periodically with the current state of the job.
    """

    @abstractmethod
    def update(self, status: models.JobProgress):
        """Abstract method to communicate the job progress to users."""


class TQDMTracker(JobProgressTracker):
    """Default tracker for the progress of the catalog build."""

    def __init__(self, tqdm_class=tqdm.tqdm):
        self.tracker = tqdm_class(desc="Catalog build", total=100, initial=0)
        self._last_progress = 0

    def update(self, status: models.JobProgress):
        if is_set(status.time_left):
            self.tracker.set_description(
                f"Catalog build (estimated time left: {render_seconds(status.time_left)})"
            )
        if is_set(status.progress):
            current = int(status.progress)
            delta = current - self._last_progress
            if delta > 0:
                self.tracker.update(delta)
                self._last_progress = current


class BuildAlreadyRunningError(Exception):
    """Exception raised when a catalog build is attempted while the previous one has not completed."""


class Builder:
    """
    Class to start a catalog build and retrieve its state.

    The catalog can be built for a specific datasource. If none is provided, the default
    datasource configured on the instance is used instead. If there is no such datasource,
    an error will be returned.
    """

    def __init__(self, client: Diapason, ds: DataSource = None):
        self.client = client.client
        self.ds = ds
        if not true_if_unset(ds.model.supports_catalog_build):
            raise ValueError(
                f"datasource {ds.get_id()} does not support catalog building"
            )

    def start(self, enqueue=False):
        """
        Starts the building of this catalog. This function is not blocking.

        If a catalog is currently building, this function will raise a `BuildAlreadyRunningError`.
        You can use `enqueue=True` to have the new catalog build start after the
        current build has fully completed..

        Args
            enqueue (bool, default False): whether to add this catalog build to
                the queue if a catalog build is ongoing. Defaults to False, in
                which case an error is raised.
        """
        if not enqueue:
            status = self.get_status()
            if status.status == "progress":
                raise BuildAlreadyRunningError()
        self._call(models.BuildCatalogAction.START)

    def pause(self):
        """Temporarily pauses the catalog build."""
        self._call(models.BuildCatalogAction.PAUSE)

    def resume(self):
        """Resumes a catalog build that was previously paused."""
        self._call(models.BuildCatalogAction.RESUME)

    def stop(self):
        """Cancels this catalog build."""
        self._call(models.BuildCatalogAction.STOP)

    def reset(self):
        """Cancels this catalog build and deletes all intermediate results."""
        self._call(models.BuildCatalogAction.RESET)

    def _call(self, action: models.BuildCatalogAction):
        resp = build_catalog.sync_detailed(
            client=self.client, data_source_id=self.ds.get_id(), action=action
        )
        validate_response(resp)

    def get_status(self) -> models.JobProgress:
        """Fetches the status of this current catalog build. Returns the raw API model."""
        resp = get_build_catalog_progress.sync_detailed(client=self.client)
        validate_response(resp)
        return resp.parsed.build_catalog_status

    def build(
        self,
        tracker: JobProgressTracker = None,
        poll_interval: float = 0.5,
        enqueue: bool = False,
        timeout: float = None,
    ) -> str:
        """Synchronously builds the catalog and waits for it to complete or stop.

        Args:
            tracker (`Tracker`, optional): a tracker object whose .update function is called at every
               iteration to communicate the progress to the user. If none is provided, a default
               tracker using TQDM (`TQDMTracker`) is used.
            poll_interval (float, optional): the time in seconds to wait between subsequent updates.
            enqueue (bool, default False): whether to add this catalog build to the queue if a catalog
                build is ongoing. Defaults to False, in which case `BuildAlreadyRunningError` is raised.
            timeout (float, optional): maximum time in seconds to wait to wait for the catalog build.
                After the timeout, this function ends in an error: the catalog build is however not
                interrupted. By default, there is no timeout.

        Returns:
            str: the final status of the catalog (one of "stop", "paused", "cancelled" or "done").
        """
        if tracker is None:
            tracker = TQDMTracker()
        starting_time = time.time()
        self.start(enqueue=enqueue)
        status = self.get_status()
        while status.status == "progress":
            time.sleep(poll_interval)
            status = self.get_status()
            tracker.update(status)
            if timeout is not None:
                if time.time() - starting_time > timeout:
                    raise TimeoutError("catalog build time exceeded timeout")
        return status.status
