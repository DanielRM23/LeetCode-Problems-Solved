# The best solution is at the end, it takes O(n)
# This first solution is not good and it's incomplete


def maxProfit(prices):
    # Find the maximum and minimum value in a range of values ginve;
    # [start, end], this is helpful later

    # First we need to find the minimum value and its index
    def findMinimum(prices, start, end):
        # It takes O(n)
        minimum = prices[start]
        index_minimum = -1
        for index in range(start, end):
            if prices[index] <= minimum:
                minimum = prices[index]
                index_minimum = index
        return minimum, index_minimum

    # Now we find the maximum
    def findMaximun(prices, start, end):
        # It takes O(n)
        maximum = prices[start]
        index_maximum = -1
        for index in range(start, end):
            if prices[index] >= maximum:
                maximum = prices[index]
                index_maximum = index
        return maximum, index_maximum

    # First, we look for the minimum value over al the interval
    start = 0
    end = len(prices)
    minimum, index_minimum = findMinimum(prices, start, end)
    maximum, index_maximum = findMaximun(prices, start, end)

    if minimum == 0 and (index_maximum < index_minimum):
        start = 0
        end = index_minimum - 1
        minimum, index_minimum = findMinimum(prices, start, end)
        start = index_minimum
        maximum, index_maximum = findMaximun(prices, start, end)

    # If the minimum is the last value, we need to look for again, excluding
    # the last one, we have a configuration such as:
    # [a_1, a_2, ... , a_n], where an is the minimum value, so the new minimum
    # could be; a_1, a_2, ..., a_n-1
    if index_minimum == end - 1:
        end = end - 1
        minimum, index_minimum = findMinimum(prices, start, end)
        start = index_minimum
        # Then, find the maximum value from [new_index, end-1]
        maximum, index_maximum = findMaximun(prices, start, end)
    else:
        # This configuration is such as [a_1, a_2, ... a_minimum, ..., a_maximum, ... a_n]
        start = index_minimum
        maximum, index_maximum = findMaximun(prices, start, end)

    return maximum - minimum


def maxProfit2(prices):
    # Solution by brute force, O(nˆ2)
    n = len(prices)
    profit = 0
    index_i = 0
    index_j = 0
    for i in range(n):
        for j in range(n):
            rest = prices[i] - prices[j]
            if rest > profit and (i > j):
                profit = rest
                index_i = i
                index_j = j

    return profit


def maxProfit3(prices):
    # If prices is empty
    if prices == []:
        return 0
    # Take the fist value, by convention, to find the minimum
    min_value = prices[0]
    # Store the profit
    max_profit = 0

    for price in prices:
        # If the price is cheaper, buy it
        if price < min_value:
            min_value = price
        # If the ganace is bigger, sell it
        elif price - min_value > max_profit:
            max_profit = price - min_value

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 5, 3, 4, 1]
prices3 = [7, 6, 4, 3, 1]
prices4 = [5, 5, 5, 5]
prices5 = [3, 2, 6, 5, 0, 3]
print(maxProfit2(prices))
