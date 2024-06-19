"""Utilities to handle input-output to and from bytes."""

import io
import pandas as pd


def data_to_bytes(data, remove_header: bool = False) -> bytes:
    """
    Converts a dataset to CSV in bytes.

    Args:
        data (any): any 2-dimensional dataset, can be a dataframe
        remove_header (bool, optional): whether the data header should be removed from the csv. Defaults to False.

    Returns:
        bytes: the csv bytes
    """
    df = pd.DataFrame(data)

    buf = io.BytesIO()
    df.to_csv(buf, index=False, header=not remove_header)
    return buf.getvalue()


def data_from_bytes(buf: bytes, no_header: bool = False) -> pd.DataFrame:
    """
    Convert a CSV-encoded dataset in bytes to a dataframe.

    Args:
        buf (bytes): the csv in byte format
        no_header (bool, optional): should be set to true if the csv bytes do not contain a header. Defaults to False.

    Returns:
        pd.DataFrame: the resulting dataframe
    """
    if no_header:
        return pd.read_csv(io.BytesIO(buf), header=None)
    return pd.read_csv(io.BytesIO(buf))


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
