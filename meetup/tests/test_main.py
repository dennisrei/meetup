from unittest import TestCase

from meetup import main


class TestMain(TestCase):

    def test_main(self):
        # Assign
        
        
        # Act
        result = main.main()

        # Assert
        self.assertEqual(result, 'Hello, World!')
