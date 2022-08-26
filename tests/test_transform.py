from unittest import TestCase
from unittest.mock import Mock, DEFAULT, patch
import pandas as pd
import datetime as dt
from meetup.transform import transform


class TestTransform(TestCase):

    def test_transfrom(self):
        # Assign
        df = pd.DataFrame({'location_code': ['LOC1', 'LOC2', 'LOC3'],
                           'measurement_time': [dt.datetime(2022, 8, 1)] * 3,
                           'bicycle_count': [10] * 3})
        aggregation_level = '1W'
        target = pd.DataFrame({'location_code': ['LOC1', 'LOC2', 'LOC3'],
                               'measurement_time': [dt.datetime(2022, 8, 7)] * 3,
                               'bicycle_count': [10] * 3,
                               'measurement_missing': [0] * 3})

        # Act
        result = transform.transform(df, aggregation_level)

        # Assert
        pd.testing.assert_frame_equal(target, result, check_dtype=False)
