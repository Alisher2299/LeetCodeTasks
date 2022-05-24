# Solution 1: dynamic programming, top-down, 𝑂(𝑛) time

def max_profit(daily_price):
    def get_bet_profit(day, have_stock):
        if day < 0:
            if not have_stock:
                return 0
            else:
                return -float('inf')
        price = daily_price[day]
        if have_stock:
            strategy_buy = get_bet_profit(day - 1, False) - price
            strategy_hold = get_bet_profit(day - 1, True)
            return max(strategy_buy, strategy_hold)
        else:
            strategy_sell = get_bet_profit(day - 1, True) + price
            strategy_avoid = get_bet_profit(day - 1, False)
            return max(strategy_sell, strategy_avoid)

    last_day = len(daily_price) - 1
    on_stock = False
    return get_bet_profit(last_day, on_stock)


arr = [7, 6, 1, 3, 1]

print('s1>', max_profit(arr))


# Solution 2: dynamic programming, bottom-up, 𝑂(𝑛) time

def max_prof(daily_price):
    cash_not_owning_share = 0
    cash_owning_share = -daily_price[0]
    for price in daily_price:
        strategy_buy = cash_not_owning_share - price
        strategy_hold = cash_owning_share

        strategy_sell = cash_owning_share + price
        strategy_avoid = cash_not_owning_share

        cash_owning_share = max(strategy_buy, strategy_hold)
        cash_not_owning_share = max(strategy_sell, strategy_avoid)

    return cash_not_owning_share


print('s2>', max_prof(arr))


def max_prof3(prices):
    max_pr = 0
    cur_min = prices[0]

    for i in range(len(prices)):
        price = prices[i]

        max_pr = max(max_pr, price - cur_min)
        cur_min = min(cur_min, price)

    return max_pr


print('s3>', max_prof3(arr))
