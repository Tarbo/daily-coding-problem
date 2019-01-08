"""
@author: Okwudili Ezeme
@date: 2019-01-08
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them
"""


def sub_list_max(aList, k):
    try:
        index = 0
        while index <= len(aList) - k:
            print(
                f'Max of sub list: {aList[index:index + k]} is {max(aList[index:index + k])}')
            index += 1
    except IndexError as err:
        print(f'>>> Please enter `k` <= {len(aList)}: {err} <<<')


# test the function
if __name__ == "__main__":
    test_list = [10, 5, 2, 7, 8, 7]
    k = 10
    sub_list_max(test_list, k)
