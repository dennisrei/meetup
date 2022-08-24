import pandas as pd
import numpy as np


def transform(
        df: pd.DataFrame,
        aggregation_level: str
) -> pd.DataFrame:
    """
    Check the following documentation for how agg works
    https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
    """

    # Check for missing values in the data
    column = 'bicycle_count'
    df.loc[df[column] == np.nan, 'measurements_missing'] = True

    df = df.groupby(['location_code', pd.Grouper(key='measurement_time', freq=aggregation_level)]).agg(
        bicycle_count=('bicycle_count', 'sum'),
        measurement_missing=('measurements_missing', 'sum')
    )

    return df
