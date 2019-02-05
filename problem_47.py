"""
@author: Okwudili Ezeme
@date: 2/5/2019
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars
"""
def max_profit(stock_list):
    stock_to_buy = 0
    max_profit = 0
    for stock in stock_list:
        for next_stock in stock_list[stock_list.index(stock):]:
            if next_stock - stock > max_profit:
                stock_to_buy = stock
                max_profit = next_stock-stock
            elif next_stock - stock == max_profit:
                continue
    return stock_to_buy

if __name__ == "__main__":
    stocks = [9, 11, 2, 5, 7, 10]
    print(f'>>> Stock to buy is: {max_profit(stocks)} <<<')