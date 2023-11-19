import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def get_current_price():
  ''' Function to retreive price'''
  # Replace with price from ChainLink function in getPrice.sol and trade.sol
  current_price = 2500.0  # Placeholder value for demonstration
  return current_price


# Function to load price data from a file
def load_price_data(file_path):
  ''' Function to load price'''
  try:
    price_data = pd.read_csv(file_path)
    return price_data
  except FileNotFoundError:
    return pd.DataFrame(
        columns=['Price'])  # Create an empty DataFrame if file doesn't exist


# Function to save price data to a file
def save_price_data(price_data, file_path):
  price_data.to_csv(file_path, index=False)


# Function to train a basic linear regression model
def train_model(price_data):
  ''' Function to retreive price'''
  X = price_data.index.values.reshape(-1, 1)
  y = price_data['Price']

  X_train, X_test, y_train, y_test = train_test_split(X,
                                                      y,
                                                      test_size=0.2,
                                                      random_state=42)

  model = LinearRegression()
  model.fit(X_train, y_train)


  return model


# Trading function using the trained model
def trade(current_price, model):
  # Example: Use the model to make trading decisions based on current price and historical data
  predicted_price = model.predict([[len(price_data)]
                                   ])  # Predict price for the next data point

  if current_price > predicted_price:
    return "Buy"
  else:
    return "Sell"

# Main function
if __name__ == "__main__":
  file_path = 'price_data.csv'
  price_data = load_price_data(file_path)

  current_price = get_current_price()
  price_data = price_data.append({'Price': current_price}, ignore_index=True)
  save_price_data(price_data, file_path)

  if len(price_data) > 1:  # Ensure enough data points for training
    model = train_model(price_data)
    trade_decision = trade(current_price, model)
    print(f"Current price: ${current_price}. Recommendation: {trade_decision}")

    # Save the trained model for future use
    with open('trained_model.pkl', 'wb') as model_file:
      pickle.dump(model, model_file)
  else:
    print("Insufficient data for training the model.")