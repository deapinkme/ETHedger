
import unittest
import pandas as pd
from ETHedger import get_current_price, load_price_data, save_price_data, train_model, trade

class TestScriptFunctions(unittest.TestCase):
    def test_get_current_price(self):
        # Test get_current_price function
        current_price = get_current_price()
        self.assertIsInstance(current_price, float)  # Ensure it returns a float value

    def test_load_and_save_price_data(self):
        # Test load_price_data and save_price_data functions
        file_path = 'test_price_data.csv'  # Test file path
        sample_data = pd.DataFrame({'Price': [100, 200, 300]})  # Sample data for testing

        # Test save_price_data function
        save_price_data(sample_data, file_path)

        # Test load_price_data function
        loaded_data = load_price_data(file_path)
        self.assertTrue(loaded_data.equals(sample_data))  # Check if loaded data matches the sample data

    def test_train_model(self):
        # Test train_model function - smoke test
        sample_data = pd.DataFrame({'Price': [100, 200, 300]})
        model = train_model(sample_data)

    def test_trade(self):
        # Test trade function
        sample_data = pd.DataFrame({'Price': [100, 200, 300]})
        model = train_model(sample_data)
        current_price = 250  # Replace with an appropriate test value

        # Ensure trade function returns 'Buy' or 'Sell'
        trade_decision = trade(current_price, model)
        self.assertIn(trade_decision, ['Buy', 'Sell'])


if __name__ == '__main__':
    unittest.main()
