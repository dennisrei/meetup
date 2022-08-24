import os

import pandas as pd
import datetime as dt

from meetup.library.database.bicycle_properties import BicycleProperties
from singleton_decorator import singleton


class BicycleDatabase:

    def __init__(self):
        self.bicycle_properties = BicycleProperties(
            os.environ.get('DB_PASSWORD'),
            os.environ.get('DB_USER'),
            os.environ.get('CONNECTION_STRING')
        )

    def retrieve_bicycle_data(
        self,
        location_id: str,
        start_date: dt.datetime,
        end_date: dt.datetime
    ) -> pd.DataFrame:
        """Returns a DataFrame with the following columns and types:
        :param str location_id: location_id of the requested measurement point
        :param dt.datetime start_date:
        :param dt.datetime end_date:
        :return: pd.DataFrame
        :raise: RetrieveException
        """
        pass

    def upload_bicycle_data(
            self,
            df: pd.DataFrame
    ):
        """Uploads a dataframe to a database:
        :param pd.DataFrame df:
        :raise: UploadException
        """
        pass


@singleton
class BicycleDatabaseAdvanced:

    def __init__(self):
        self.bicycle_properties = BicycleProperties(
            os.environ.get('DB_PASSWORD'),
            os.environ.get('DB_USER'),
            os.environ.get('CONNECTION_STRING')
        )

    def retrieve_bicycle_data(
            self,
            location_id: str,
            start_date: dt.datetime,
            end_date: dt.datetime
    ) -> pd.DataFrame:
        """Returns a DataFrame with the following columns and types:
        :param str location_id: location_id of the requested measurement point
        :param dt.datetime start_date:
        :param dt.datetime end_date:
        :return: pd.DataFrame
        :raise: RetrieveException
        """
        pass

    def upload_bicycle_data(
            self,
            df: pd.DataFrame
    ):
        """Uploads a dataframe to a database:
        :param pd.DataFrame df:
        :raise: UploadException
        """
        pass
