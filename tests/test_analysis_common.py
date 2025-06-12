import importlib
import os

import pandas as pd


def test_analysis_modules_common_properties():
    # Create dummy data
    series = pd.Series([1.0, 2.0, 3.0, 4.0])
    # Load and test the analysis modules
    analysis_dir = os.path.join(os.path.dirname(__file__), "../app/analysis")
    for filename in os.listdir(analysis_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"app.analysis.{module_name}")
            # Module should have a compute function
            assert hasattr(module, "compute"), f"{module_name} has no 'compute()'"
            # The compute function should return a float type
            result = module.compute(series)
            assert isinstance(result, float), f"{module_name}.compute() must return float, got {type(result)}"
