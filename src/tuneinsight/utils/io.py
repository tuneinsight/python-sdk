"""Utilities to handle input-output to and from bytes."""

import pandas as pd


def generate_csv_records(path: str, chunk_size: int = 4096):
    """
    Returns a dataframe generator / iterator that allows to easily iterate over chunks of the dataframe.

    Args:
        path (str): path to the csv file to convert to the dataframe iterator.
        chunk_size (int, optional): The chunk size to use. Defaults to 4096.

    Yields:
        Generator[pd.DataFrame]: A generator / iterator returning chunks of the dataframe.
    """
    return pd.read_csv(path, chunksize=chunk_size)


def generate_dataframe_chunks(data: pd.DataFrame, chunk_size: int = 4096):
    """
    Returns a generator that allows to easily iterate over chunks of the dataframe.

    Args:
        data (pd.DataFrame): The dataframe to chunk.
        chunk_size (int, optional): The chunk size to use. Defaults to 4096.

    Yields:
        Generator[pd.Dataframe]: A generator / iterator returning chunks of the dataframe.
    """
    total_rows = len(data)
    for start in range(0, total_rows, chunk_size):
        yield data[start : start + chunk_size]
