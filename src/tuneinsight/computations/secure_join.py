from typing import List
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner


class SampleExtraction(ComputationRunner):
    """Computation for a Sample Extraction.

    Args:
        ComputationRunner (ComputationRunner): parent class for running computation through the REST API.
    """

    join_id: str = ""

    def get_sample(self,sample_size: int = 1,seed: str = "default-seed") -> pd.DataFrame:
        """ Extract a sample from the data.

        Args:
            sample_size (int, optional): size of the sample as number of rows. Defaults to 1.
            seed (str, optional): seed to use for the sampling. Defaults to "default-seed".

        Raises:
            Exception: if the join_id is not set.

        Returns:
            pd.DataFrame: resulting sample.
        """
        if self.join_id == "":
            raise Exception("join id must be set")
        comp = models.SampleExtraction(type=models.ComputationType.SAMPLEEXTRACTION)
        comp.sample_size = sample_size
        comp.seed = seed
        comp.join_id = self.join_id
        results = super().run_computation(comp=comp,local=False,keyswitch=True,decrypt=True)
        df = results[0].get_dataframe()
        return df


class SecureJoin(ComputationRunner):
    """ Perform a distributed join.

    Args:
        ComputationRunner (ComputationRunner): parent class for running computation through the REST API.

    Raises:
        Exception: if the join_id is not set.
    """


    join_id: str = ""



    def create(self, target_columns: List[str], join_columns: List[str]):
        """ Create a dataset from a distributed join.

        Args:
            target_columns (List[str]): column names of target columns
            join_columns (List[str]): column names to join the data on
        """

        model = models.DistributedJoin(type=models.ComputationType.DISTRIBUTEDJOIN)
        model.target_columns = target_columns
        model.join_columns = join_columns
        model.project_id = self.project_id
        model.missing_patterns = ["","NaN"]
        dataobjects = super().run_computation(comp=model,local=False,keyswitch=False,decrypt=False)
        self.join_id = dataobjects[0].get_id()

    def new_sample_extraction(self) -> SampleExtraction:
        """ Create a Sample Extraction computation.

        Raises:
            Exception: if the join_id is not set.

        Returns:
            SampleExtraction: resulting computation.
        """
        if self.join_id == "":
            raise Exception("join must be created before extracting a sample")
        sample_ext = SampleExtraction(client=self.client, project_id=self.project_id)
        sample_ext.join_id = self.join_id
        return sample_ext
