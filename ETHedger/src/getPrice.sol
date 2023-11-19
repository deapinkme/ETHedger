// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "chainlink/interfaces/AggregatorV3Interface.sol";

contract EthPriceConsumer {
    AggregatorV3Interface internal priceFeed;

    constructor() {
        // Replace this address with the relevant ETH/USD price feed contract address on the Ethereum mainnet or the respective testnet
        priceFeed = AggregatorV3Interface(0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419);
    }

    function getEthPrice() external view returns (int) {
        (, int price, , , ) = priceFeed.latestRoundData();
        return price;
    }
}