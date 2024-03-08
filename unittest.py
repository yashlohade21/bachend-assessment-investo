import unittest
import pandas as pd

class TestDataValidation(unittest.TestCase):

    def test_valid_data_types(self):
        # Assuming you have a function to fetch and preprocess the data
        data = fetch_data()

        # Check data types
        self.assertTrue(data['open_price'].dtype == float)
        self.assertTrue(data['high_price'].dtype == float)
        self.assertTrue(data['low_price'].dtype == float)
        self.assertTrue(data['close_price'].dtype == float)
        self.assertTrue(data['volume'].dtype == int)
        self.assertTrue(data['instrument'].dtype == str)
        self.assertTrue(data['datetime'].dtype == pd.Timestamp)

if __name__ == '__main__':
    unittest.main()
