import pandas as pd

from app.analysis import mean


def test_mean_compute():
    # Create a sample pandas Series
    series = pd.Series([1.0, 2.0, 3.0, 4.0])
    
    # Compute the mean using the compute function
    result = mean.compute(series)
        
    # Assert that the computed mean is correct
    expected_mean = (1.0 + 2.0 + 3.0 + 4.0) / 4
    assert result == expected_mean, f"Expected {expected_mean}, got {result}"

    # Assert NaN handling for empty series
    empty_series = pd.Series([])
    result_empty = mean.compute(empty_series)
    assert pd.isna(result_empty), f"Expected NaN for empty series, got {result_empty}"