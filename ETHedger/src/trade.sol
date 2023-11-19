// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "forge-std/console.sol";
import "chainlink/interfaces/AggregatorV3Interface.sol";

contract TradeRecord {
    AggregatorV3Interface public priceFeed;
    
    struct Trade {
        uint256 blockId; // blockId is non-negative
        int256 amount; // amount is negative on sell, positive on buy
    }

    constructor () {
        priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
    }
    
    // Arrays to store buy and sell trades and their corresponding amounts
    Trade[] public trades;

     // Events for logging buy and sell trades
    event BuyTrade(uint256 indexed blockId, int256 amount);
    event SellTrade(uint256 indexed blockId, int256 amount);
   
    // Function to record a buy trade and its amount
    function recordBuyTrade(int256 amount) external {
        // Simulated buy trade logic - replace this with actual trade execution
        trades.push(Trade(block.number, amount));
        emit BuyTrade(block.number, amount);
    }
    // Function to record a sell trade and its amount
    function recordSellTrade(int256 amount) external {
        // Simulated sell trade logic - replace this with actual trade execution
        trades.push(Trade(block.number, amount));
        emit SellTrade(block.number, amount);
    }

    // Function to get ETH price from chainlink
    function getPrice() public view returns (uint256 price) {
        (, int256 p, , , ) = priceFeed.latestRoundData();
        require(p > 0, "Invalid price"); // Reverts, peventing liquidations at invalid price
        return uint256(p);
    }
}