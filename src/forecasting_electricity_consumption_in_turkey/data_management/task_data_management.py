"""Tasks for managing the data."""

import pandas as pd
import pytask

from forecasting_electricity_consumption_in_turkey.config import BLD, SRC
from forecasting_electricity_consumption_in_turkey.data_management import clean_data
from forecasting_electricity_consumption_in_turkey.utilities import read_yaml


@pytask.mark.depends_on(
    {
        "scripts": ["clean_data.py"],
        "data_info": SRC / "data_management" / "data_info.yaml",
        "data": SRC / "data" / "data.csv",
    },
)
@pytask.mark.produces(BLD / "python" / "data" / "data_clean.csv")
def task_clean_data_python(depends_on, produces):
    """Clean the data (Python version)."""
    data_info = read_yaml(depends_on["data_info"])
    data = pd.read_csv(depends_on["data"])
    data = clean_data(data, data_info)
    data.to_csv(produces, index=False)
