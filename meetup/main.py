import datetime as dt

import pandas as pd

from meetup.library.database.bicycle_database import BicycleDatabase
from meetup.library.exceptions.exceptions import UploadException, RetrieveException
from meetup.transform import transform


def main(
        location_id: str,
        start_date: dt.datetime,
        end_date: dt.datetime,
        aggregation_level: str
):
    # Retrieve the data from the database
    try:
        bicycle_database = BicycleDatabase()
        bicycle_df = bicycle_database.retrieve_bicycle_data(location_id, start_date, end_date)
        # bicycle_df = pd.read_csv('resources/bicycle-data-export.csv')
    except RetrieveException as exc:
        raise Exception(f'Could not retrieve data due to: {exc}')

    # Transform the data
    bicycle_transformed_df = transform.transform(bicycle_df, aggregation_level)
    # Upload the data to the database
    try:
        bicycle_database.upload_bicycle_data(bicycle_transformed_df)
    except UploadException as exc:
        raise Exception(f'Could not upload data due to: {exc}')


if __name__ == '__main__':
    main('location_A', dt.datetime(2022, 8, 1), dt.datetime(2022, 8, 30), '1W')
