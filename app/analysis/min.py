import pandas as pd


def compute(series: pd.Series) -> float:
    """Compute the minimum of a pandas Series.

    Args:
        series (pd.Series): Input series to compute the minimum.

    Returns:
        float: The minimum of the series.

    """
    return series.min()
