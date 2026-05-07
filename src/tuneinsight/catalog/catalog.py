"""Utilities to connect to a catalog on a Tune Insight instance."""

from typing import Generator

from tuneinsight import models
from tuneinsight.client import Diapason
from tuneinsight.client.validation import validate_response

from tuneinsight.api.sdk.types import value_if_unset
from tuneinsight.api.sdk.api.api_ontology import get_ontology_search, get_care_sites

DEFAULT_ONTOLOGIES = ["ICD10", "ATC", "LOINC", "CHOP", "SNOMED"]


class Catalog:
    """Class to interact with the catalog available on a Tune Insight instance."""

    def __init__(self, client: Diapason):
        self.client = client.client

    def get_care_sites(self) -> list[models.CareSite]:
        """Retrieves the list of care sites available in the instance."""
        resp = get_care_sites.sync_detailed(
            client=self.client,
        )
        validate_response(resp)
        return resp.parsed

    # pylint: disable=dangerous-default-value
    def search(
        self,
        query: str = "",
        ontologies=DEFAULT_ONTOLOGIES,
        with_occurrence: bool = False,
        with_network_occurrence: bool = False,
        page: int = 1,
        per_page: int = 20,
        care_sites: list[str] = None,
    ) -> dict[str, models.Term]:
        """Searches the catalog for all terms matching a string.

        Args:
            query (str, optional): the string to search for. Defaults to "", in which case all terms are fetched.
            ontologies (list, optional): the list of ontologies to search for the term. Defaults to the five
                default ontologies (which may not be present in your data).
            with_occurrence (bool, optional): whether to only include terms that have an occurrence (>= 10 patients).
                Defaults to False (terms not in the data will also be included).
            with_network_occurrence (bool, optional): whether to only include terms that have an occurrence (>= 10
                patients) in the network. Defaults to False (terms not in the data will also be included).
            page (int, optional): if there are many results, page number to retrieve. Defaults to 1.
            per_page (int, optional): number of terms to include per "page". Defaults to 20.
            care_sites (list of strings, optional): the names of the care sites for which the catalog is fetched.
                If more than one care site is provided, occurrences from different care sites are aggregated
                together. If not provided, catalogs from all care sites are retrieved and aggregated.

        Returns:
            dict[str, models.Term]: for each ontology, the list of terms retrieved (up to `page` terms).
        """
        # Allow users to provide models.CareSite instead of strings.
        if care_sites is not None:
            care_sites = [
                cs.name if isinstance(cs, models.CareSite) else cs for cs in care_sites
            ]
        resp = get_ontology_search.sync_detailed(
            client=self.client,
            query=query,
            ontologies=ontologies,
            with_occurrence=with_occurrence,
            with_network_occurrence=with_network_occurrence,
            page=page,
            per_page=per_page,
            care_sites=care_sites,
        )
        validate_response(resp)
        results: list[models.GetOntologySearchResponse200Item] = resp.parsed
        terms_by_ontology = {o: [] for o in ontologies}  # Safe default.
        for res in results:
            terms_by_ontology[res.ontology] = value_if_unset(res.results, [])
        return terms_by_ontology

    def browse(
        self,
        query: str,
        ontology: str,
        with_occurrence: bool = False,
        care_sites: list[str] = None,
    ) -> Generator[models.Term, None, None]:
        """
        Retrieves all the terms for a query in an ontology, as an iterator.

        Terms are fetched lazily, page by page, until all terms have been read.

        Args:
            query (str): the string to search for. If empty (""), all terms are fetched.
            ontologies (list): the ontology to search for this term.
            with_occurrence (bool, optional): whether to only include terms that have an occurrence (>= 10 patients).
                Defaults to False (terms not in the data will also be included).
            care_sites (list of strings, optional): the names of the care sites for which the catalog is fetched.
                If more than one care site is provided, occurrences from different care sites are aggregated
                together. If not provided, catalogs from all care sites are retrieved and aggregated.

        Yields:
            models.Term: the terms fetches from the catalog.
        """
        page = 1
        per_page = 50
        while True:
            result = self.search(
                query=query,
                ontologies=[ontology],
                page=page,
                per_page=per_page,
                with_occurrence=with_occurrence,
                care_sites=care_sites,
            )
            terms = result[ontology]
            yield from terms
            if len(terms) < per_page:
                break
            page += 1
