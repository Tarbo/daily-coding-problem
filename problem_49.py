"""
@author: Okwudili Ezeme
@date: 2019-02-08

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
"""


def max_sum(a_list):
    max_sum = 0
    sub_array = None
    for value in a_list:
        if sum(a_list[a_list.index(value):]) > max_sum:
            max_sum = sum(a_list[a_list.index(value):])
            sub_array = a_list[a_list.index(value):]
    return max_sum, sub_array


if __name__ == "__main__":
   # array = [34, -50, 42, 14, -5, 86]
    array = [-5, -1, -8, -9]
    max_sum, sub_array = max_sum(array)
    print(f'>>> maximum sum: {max_sum} <<<\n>>> sub array: {sub_array} <<<')
