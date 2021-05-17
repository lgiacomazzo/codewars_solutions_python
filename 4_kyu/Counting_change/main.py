from tests.tests import tests

"""
def count_change(money, coins):
    if money <= 0:
        return 0
    
    def _count_change(money, index):
        if money == 0:
            return 1
        correct_comb = 0
        for i in range(index, len(coins)):
            if money >= coins[i]:
                print("From {} - {} in iteration {} with index {}".format(money, coins[i], i, index))
                correct_comb += _count_change(money - coins[i], index=i)
        print("Correct combinations found: {}".format(correct_comb))
        return correct_comb
    
    return _count_change(money, index=0)
"""
# https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/
def count_change(amount, coins):
    ways = [1] + [0] * amount
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]


if __name__ == "__main__":
    for money, coins, result in tests:
        if count_change(money, coins) == result:
            print("ok for " + str(money))
        else:
            print("wrong for " + str(money))
