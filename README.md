# ETHedger

## What is ETHedger

The process begins with a simple machine learning linear regression model coded in Python, leveraging libraries such as Pandas and Scikit-learn. This model utilizes the price data of Ethereum (ETH) fetched from **Chainlink**. This price information is then integrated into the **Cartesi VM**, a virtual machine where the Python script named ETHedger operates.

Within this environment, the script tracks and records the buying and selling actions performed. These transactions are logged onto a recorder. At the conclusion of each epoch, a thorough check of the log record takes place. If the logged data is deemed valid based on predefined criteria, the depositor—individual or entity initiating the transactions—is refunded their initial deposit. However, if the logged data fails to meet the validation criteria, the deposit is claimed by the trader or program responsible for executing these transactions.

The functionality for executing buy, sell, and price-related actions resides within the Solidity smart contract. This smart contract serves as the foundational structure enabling the execution of these functionalities within the Ethereum blockchain network. Through this contract, the logic governing the deposit refunds or claims based on the validity of the transaction records is enforced.

In summary, this ecosystem involves a linear regression model utilizing ETH price data sourced from **Chainlink**, processing within the **Cartesi VM** via the Python script ETHedger, transaction logging, validation checks, and deposit management executed through a Solidity smart contract within the Ethereum blockchain network.

## What should I be looking for?

- ETHedger
    -ETHedger
        - src
            - **getPrice.sol** → ETH tick price smart contract with ChainLink
            - **price_data.csv** → locally stored data of observered ticks
            - **trade.sol** → smart contract for buy, sell and ETH tick price
            - **trained_model.pkl** → ML model that has been trained
        - test
            - **test_ETHedger.py** → unit tests for ETHedger.py
        - trading_model
            - **ETHedger.py** → ML python script
            - **requirements.txt** → text file of requirements


## How it works

[PRESENTATION](https://www.intel.com)
