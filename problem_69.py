"""
@author: Okwudili Ezeme
@date: 2019-02-28
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's - 10 * -10 * 5.

You can assume the list has at least three integers.
"""
from operator import mul
from functools import reduce


def max_subseq_product(sequence, sub_seq_size):
    if len(sequence) < sub_seq_size:
        return 0
    sequence = sorted(sequence)
    # product of last 3 elements
    right_subseq_prod = reduce(mul, sequence[-sub_seq_size:], 1)
    # product of first 2 elements and the last one
    left_subseq_prod = reduce(mul, [sequence[0], sequence[1], sequence[-1]], 1)
    return max(right_subseq_prod, left_subseq_prod)


if __name__ == "__main__":
    sequence = [-10, -10, 5, 2]
    sub_size = 3
    print(
        f'>>> Max {sub_size} sub sequence value is: {max_subseq_product(sequence,sub_size)}')
