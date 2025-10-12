
from typing import List

def maxProfit(arr: List[int]) -> int:
    maxPro = 0
    n = len(arr)


    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                maxPro = max(arr[j] - arr[i], maxPro)


    return maxPro


def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)




'''
Problem
You are given an array where the ith element is the price of a given stock on day i. You want to 
maximize your profit by choosing a single day to buy one stock and choosing a different day in the 
future to sell that stock. Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.
'''

def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print("Maximum profit:", maxProfit(prices))  # Output: 5

