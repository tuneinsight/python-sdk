import io
import pandas as pd


def data_to_bytes(data, remove_header: bool = False) -> bytes:
    """
    data_to_bytes converts a dataset to csv bytes

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
    data_from_bytes convert the provided csv bytes to a dataframe

    Args:
        buf (bytes): the csv in byte format
        no_header (bool, optional): should be set to true if the csv bytes do not contain a header. Defaults to False.

    Returns:
        pd.DataFrame: the resulting dataframe
    """
    if no_header:
        return pd.read_csv(io.BytesIO(buf), header=None)
    return pd.read_csv(io.BytesIO(buf))
