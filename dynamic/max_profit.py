def maxProfit(prices) -> int:
    min_price = float('inf')
    max_delta = 0
    for price in prices:
        min_price = min(min_price, price)
        current_delta = price - min_price
        max_delta = max(max_delta, current_delta)
    return max_delta


if __name__ == '__main__':
    result1 = maxProfit([3, 1, 7, 9, 8])
    print(result1)
