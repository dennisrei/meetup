from unittest import TestCase
from unittest.mock import Mock, DEFAULT, patch

import pandas as pd
import datetime as dt

from meetup.library.exceptions.exceptions import UploadException, RetrieveException


from meetup import main


@patch.multiple(main.__name__, BicycleDatabase=DEFAULT)
class TestMain(TestCase):

    def test_main(self, BicycleDatabase):
        # Assign
        location_id = 'LOC1'
        BicycleDatabase().retrieve_bicycle_data.return_value = \
            pd.DataFrame({'location_code': ['LOC1'] * 3,
                           'measurement_time': [dt.datetime(2022, 8, 1)] * 3,
                           'bicycle_count': [10] * 3})
        start_date = dt.datetime(2022, 8, 1)
        end_date = dt.datetime(2022, 8, 2)
        aggregation_level = '1W'

        # Act
        main.main(location_id, start_date, end_date, aggregation_level)

        # Assert
        BicycleDatabase().retrieve_bicycle_data.assert_called()
        BicycleDatabase().upload_bicycle_data.assert_called()

    def test_main_download_exception(self, BicycleDatabase):
        # Assign
        location_id = 'LOC1'
        BicycleDatabase().retrieve_bicycle_data.side_effect = RetrieveException
        start_date = dt.datetime(2022, 8, 1)
        end_date = dt.datetime(2022, 8, 2)
        aggregation_level = '1W'

        # Act & Assert
        with self.assertRaises(Exception):
            main.main(location_id, start_date, end_date, aggregation_level)

    def test_main_upload_exception(self, BicycleDatabase):
        # Assign
        location_id = 'LOC1'
        BicycleDatabase().retrieve_bicycle_data.return_value = \
            pd.DataFrame({'location_code': ['LOC1'] * 3,
                           'measurement_time': [dt.datetime(2022, 8, 1)] * 3,
                           'bicycle_count': [10] * 3})
        BicycleDatabase().upload_bicycle_data.side_effect = UploadException
        start_date = dt.datetime(2022, 8, 1)
        end_date = dt.datetime(2022, 8, 2)
        aggregation_level = '1W'

        # Act & Assert
        with self.assertRaises(Exception):
            main.main(location_id, start_date, end_date, aggregation_level)
