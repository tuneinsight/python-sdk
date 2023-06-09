import csv
import unittest
from typing import Any, List, Tuple
import pandas as pd
import numpy as np
from tuneinsight.api.sdk.types import Response
from tuneinsight.utils.generator import PatientGenerator
from tuneinsight.client.diapason import Diapason

class TestCase3Nodes(unittest.TestCase):
    """
    TestCase3Nodes is a base test case class to test the SDK with a 3 node configuration
    """


    generator: PatientGenerator = None
    clients: List[Diapason] = None
    root_node: Diapason = None
    num_nodes: int = 3
    delta: float = 0.0001
    test_data_path: str = "test/data/tiny.csv"

    def verify_success(self,response: Response):
        status_codes_min = 200
        status_codes_max = 210
        if response.status_code < status_codes_min or response.status_code > status_codes_max:
            print("wrong status code: ",response.content)
        self.assertGreaterEqual(response.status_code,status_codes_min)
        self.assertGreater(status_codes_max,response.status_code)

    @staticmethod
    def aggregate_data(data):
        new_data = []
        result_row = []
        vec_length = len(data[0])
        for i in range(vec_length):
            result_row.append(float(0))
        for row in data:
            for i,v in enumerate(row):
                result_row[i] += float(v)
        new_data.append(result_row)
        return new_data


    @staticmethod
    def concatenate_rows(datas):
        new_data = []
        for data in datas:
            for row in data:
                new_data.append(row)
        return new_data


    def aggregate_matrices(self,datas):
        tmp = self.concatenate_rows(datas)
        return self.aggregate_data(tmp)



    def floats_equal(self,v1: float,v2: float):
        """
        floats_equal compares two float values and allows an error equal to delta

        Args:
            v1 (float): the first value to compare
            v2 (float): the second value to compare
        """
        self.assertGreater(self.delta,abs(float(v1) - float(v2)))


    def vals_equal(self,v1: Any,v2: Any):
        """
        vals_equal compares equality between two values if the two values are declared as non equal, then it checks wether their float
        representations match

        Args:
            v1 (Any): the first value to compare
            v2 (Any): the second value to compare
        """
        if v1 != v2:
            self.floats_equal(v1,v2)

    def compare_data(self,vals1: List[List[Any]],vals2: List[List[Any]]):
        """
        compare_data compares two matrices and asserts equality for dimensions and values

        Args:
            vals1 (List[List[Any]]): the first matrix to compare
            vals2 (List[List[Any]]): the second matrix to compare
        """
        self.assertEqual(len(vals1),len(vals2))
        for i,row in enumerate(vals1):
            self.assertEqual(len(row),len(vals2[i]))
            for j,v in enumerate(row):
                self.vals_equal(v,vals2[i][j])


    def compare_csv(self,expected_cols: List[str],actual_cols: List[str],expected_vals: List[List[Any]],actual_vals: List[List[Any]]):
        self.compare_data([expected_cols],[actual_cols])
        self.compare_data(expected_vals,actual_vals)

    @staticmethod
    def get_csv(filename: str,with_header: bool = True) -> Tuple[List[str],List[List[str]]]:
        """
        get_csv reads a csv

        Args:
            filename (str): the path to the csv file
            with_header (bool, optional): indicates whether or not the csv file contains column header. Defaults to True.

        Returns:
            Tuple[List[str],List[List[str]]]: a tuple with the columns followed by the data
        """
        columns = []
        data = []
        with open(filename,encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in reader:
                if line_count == 0 and with_header:
                    columns = row
                    line_count += 1
                else:
                    data.append(row)
                    line_count += 1
        return columns,data


    def setUp(self):
        """
        setUp sets up the clients and other variables before running the test case
        """
        # Setup the clients to be used in other test case
        self.clients = []
        # Setup client for each node with 'test' user
        for i in range(self.num_nodes):
            path = "test/configs/conf_" + str(i) + ".yml"
            client = Diapason.from_config_path(path)
            self.clients.append(client)
        self.root_node = self.clients[0]
        self.generator = PatientGenerator()
        self.generator.seed("test")
        self.generator.age_ranges = [[2,12],[13,20],[20,35],[35,55],[55,80],[80,110]]
        self.generator.age_weights = [1,2,3,3,2,1]
        self.generator.district_weights = [10,5,1,1,1]
        self.generator.age_height_ranges = [10,20,50,80,110]
        self.generator.age_height_averages = [100,165,185,165,160]
        self.generator.gender_weights = [50,50,1,1]
        self.generator.origin_weights = [5,10,1,1,10,10,1]




def partition_dataframe(df: pd.DataFrame,num: int = 3,seed: int=0) -> List[pd.DataFrame]:
    if num == 1:
        return [df]
    if num > len(df):
        raise ValueError("number of partitions cannot be higher then the row count")
    part_size = int(len(df) / num)
    partition = df.sample(n=part_size,random_state=seed)
    remaining = df.drop(index=partition.index)
    partitions = partition_dataframe(remaining,num-1,seed)
    partitions.append(partition)
    return partitions


def sigmoid(z: np.ndarray) -> np.ndarray:
    '''
    sigmoid applies the sigmoid activation on z

    Args:
        z (np.ndarray): the numpy representation of z

    Returns:
        np.ndarray: the transformed array
    '''
    return 1 / (1 + np.exp(-z))

def regression_prediction(weights: np.ndarray,bias: np.ndarray,inputs: np.ndarray,activation: callable = None) -> np.ndarray:
    '''
    regression_prediction computes the regression prediction given the weights, bias and input datasets. An additional optional
    activation function can be provided to be applied after the linear transformation

    Args:
        weights (np.ndarray): the model weights/coefficients
        bias (np.ndarray): the model bias
        inputs (np.ndarray): the input dataset
        activation (callable, optional): the optional activation function. Defaults to None.

    Returns:
        np.ndarray: the numpy array of predicted values
    '''
    z = np.dot(weights.T,inputs.T) + bias
    if activation is not None:
        return activation(z)
    return z
