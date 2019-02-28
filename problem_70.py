"""
@author: Okwudili Ezeme
@date: 2019-02-28
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def perfect_number(n):
    # get the product of n+1 and 10
    assert n > 1, "n must be greater than one"
    # gives you the next number with modulus zero when divided by 10
    value = (n + 1) * 10
    return value - n


if __name__ == "__main__":
    n = 6
    print(f'>>> n-th perfect number for {n} is: {perfect_number(n)}')
