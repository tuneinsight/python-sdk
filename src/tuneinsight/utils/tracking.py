"""Utilities to track the progress of ongoing tasks."""

from typing import Union

import random
import string
import time
import threading
import tqdm

from tuneinsight.client.validation import validate_response
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk.types import value_if_unset
from tuneinsight.api.sdk.api.api_python_server import track_python_server_task


def new_task_id():
    """
    Produces a valid unique identifier for a task.

    Unicity of the identifier is not guaranteed (since the server is not reached), but
    collision is extremely unlikely, as identifiers are random hexadecimal strings of
    length 32.
    """
    return "".join(random.choices(string.hexdigits, k=32))


class ProgressTracker:
    """
    Synchronously tracks the progress of a task, using a tqdm display for the user.

    Args
        task_id: the unique identifier of the task being tracked.
        tqdm_class: the tqdm class to use to display progress (default is tqdm.tqdm).
    """

    def __init__(self, task_id, tqdm_class=tqdm.tqdm):
        self.task_id = task_id
        self.new_tqdm = tqdm_class
        # Internal variables representing the current state being displayed (none to begin with).
        self.current_phase = None  # Current phase of the task.
        self.tqdm = None  # Current tracker.
        self.previous_step = 0  # Steps done so far in the current phase.
        self.running = False  # Whether both the task and tracker are running.

    def show(self, tp: models.TaskProgress):
        """Updates the current display for the given task progress."""
        # Modify in-place the task progress to be nicer to use.
        tp.num_stages = value_if_unset(tp.num_stages, 1)
        tp.num_steps = value_if_unset(tp.num_steps, 1)
        tp.step_number = value_if_unset(tp.step_number, 0)
        tp.stage_number = value_if_unset(tp.stage_number, 0)
        # If we enter a new phase, swap to a new tracker.
        if self.current_phase != tp.stage_number:
            self.current_phase = tp.stage_number
            self._cleanup()
            description = f"{tp.stage_name} [{tp.stage_number}/{tp.num_stages}] "
            self.tqdm = self.new_tqdm(
                desc=description, total=tp.num_steps, initial=tp.step_number
            )
            self.tqdm.display()
        else:
            # Update the current tracker by the change since previous update.
            self.tqdm.update(tp.step_number - self.previous_step)
        # Update
        self.previous_step = tp.step_number

    def start(
        self,
        client: Union["Diapason", Client],
        step: float = 0.1,
        tolerate_errors: int = 10,
    ):
        """
        Synchronously starts the progress tracking process.

        Args:
            client: the client used to connect to the instance.
            step (float, default 0.1): time to wait between queries to the server.
            tolerate_errors (int, default 10): number of errors to (silently) tolerate
                before interrupting. This is typically used when there is a delay between
                the creation of the unique ID and the task starting on the server.

        """
        if not isinstance(client, Client):  # Assume this is a Diapason
            client: Client = client.client
        self.running = True
        num_errors = 0
        while self.running:
            # Get the current status of the task progress.
            resp = track_python_server_task.sync_detailed(self.task_id, client=client)
            try:
                validate_response(resp)
            except LookupError as err:
                num_errors += 1
                time.sleep(0.5)
                if num_errors > tolerate_errors:
                    raise err
            else:
                tp: models.TaskProgress = resp.parsed
                self.show(tp)
                self.running = tp.running
            time.sleep(step)
        self._cleanup()

    def start_background(self, *args, **kwargs):
        """Asynchronously tracks the progress (see start for arguments)."""
        threading.Thread(target=lambda: self.start(*args, **kwargs)).start()

    def stop(self):
        """Stops an ongoing progress tracking."""
        self.running = False

    def _cleanup(self):
        if self.tqdm is not None:
            self.tqdm.close()
        self.previous_step = 0
