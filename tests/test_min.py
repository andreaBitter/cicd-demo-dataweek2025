import pandas as pd

from app.analysis import min


def test_min_compute():
    # Create a sample pandas Series
    series = pd.Series([1.0, 2.0, 3.0, 4.0])
    
    # Compute the min using the compute function
    result = min.compute(series)
        
    # Assert that the computed min is correct
    expected_min = 1.0
    assert result == expected_min, f"Expected {expected_min}, got {result}"

    # Assert NaN handling for empty series
    empty_series = pd.Series([])
    result_empty = min.compute(empty_series)
    assert pd.isna(result_empty), f"Expected NaN for empty series, got {result_empty}"
