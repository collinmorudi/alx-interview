# 0x08-making_change

This directory contains a solution to the "Change comes from within" task, which involves calculating the minimum number of coins needed to make a given amount of change.

## Task Description

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

**Prototype:** `def makeChange(coins, total)`

**Return:** Fewest number of coins needed to meet total.

* If total is 0 or less, return 0.
* If total cannot be met by any number of coins you have, return -1.
* coins is a list of the values of the coins in your possession.
* The value of a coin will always be an integer greater than 0.
* You can assume you have an infinite number of each denomination of coin in the list.

## Implementation

The solution uses dynamic programming to efficiently calculate the minimum number of coins. It creates a list to store the minimum coins needed for each amount up to the total, and iteratively updates this list based on the available coin denominations.

## Usage

The `makeChange` function can be used as follows:

```python
>>> makeChange([1, 2, 25], 37)
7
>>> makeChange([1256, 54, 48, 16, 102], 1453)
-1
