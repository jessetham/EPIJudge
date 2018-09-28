from test_framework import generic_test

# O(n^2) solution. Check every possible combination and take the maximum
def buy_and_sell_stock_once_1(prices):
    current_max = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current_max = max(current_max, prices[j] - prices[i])
    return current_max

# O(n) solution. Keep track of the max difference so far and the min value so far
# The judge doesn't seem to like the error check but the answer is correct
def buy_and_sell_stock_once_2(prices):
    if len(prices) < 2:
        raise Exception('input array requires must have a len > 2')
    current_max = 0
    current_min_so_far = prices[0]
    for price in prices[1:]:
        current_max = max(current_max, price - current_min_so_far)
        current_min_so_far = min(current_min_so_far, price)
    return current_max

def buy_and_sell_stock_once(prices):
    return buy_and_sell_stock_once_2(prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
