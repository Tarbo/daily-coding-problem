"""
@author: Okwudili Ezeme
@date: 01-06-2019
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible
"""

import numpy as np


class OrderIDs():
    def __init__(self, N):
        self.log = [None] * N

    def record(self, order_id):
        "The oldest `order_id` is always at the end of the list"
        self.log = [order_id] + self.log[:-1]

    def get_last(self, index):
        "`index` is the ith last element"
        try:
            return self.log[index]
        except IndexError as err:
            print(
                f'>>> Enter index within 0 -- {len(self.log)-1} \t {err} <<<')


if __name__ == "__main__":
    orderID = OrderIDs(10)
    np.random.seed(100)
    test_ids = np.random.randint(20, 1000, 40)
    print(f'>>> Log contains:{test_ids}')
    for order_id in test_ids:
        orderID.record(order_id)
    print(orderID.get_last(0))
    print({orderID.get_last(56)})
