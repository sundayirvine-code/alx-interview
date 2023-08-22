#!/usr/bin/python3
"""
Make Cahnge module
"""

def makeChange(coins, total):
    """
    Calculate the minimum number of coins required to make up a given total amount.

    Args:
        coins (list of int): A list of coin denominations available for making change.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins required to make up the total amount.
             Returns -1 if it's not possible to make the exact change using the given coins.
    
    Algorithm: Make Change

        1. Define the makeChange function with two parameters: coins (list of coin denominations) and total (the target amount).
        2. Initialize a variable coin_number to 0, which will store the minimum number of coins needed to make change.
        3. Sort the coins list in descending order to start with the largest coin denominations.
        4. Iterate through each coin in the coins list:
            a. While the total is greater than or equal to the current coin value, subtract the coin value from the total and increment coin_number.
            b. Repeat this process until the total becomes less than the current coin value.
        5. After the loop, check if the total amount is exactly 0:
            a. If it is 0, return the value of coin_number, indicating the minimum number of coins needed.
            b. If it's not 0, return -1, indicating that it's not possible to make the exact change using the given coins.
        6. End of the makeChange function.

    """
    if total <= 0:
        return 0
    if len(coins) <= 0:
        return -1
    coin_number = 0
    
    # Sort in descending order
    coins.sort(reverse=True)
    
    for coin in coins:
        while total >= coin:
            total -= coin
            coin_number += 1
    
    if total == 0:
        return coin_number
    else:
        return -1
