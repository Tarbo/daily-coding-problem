"""
@author: Okwudili Ezeme
@question:
    This problem was asked by Uber.

    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
"""


def problem_2(aList):
    try:
        new_list = []
        for idx in range(len(aList)):
            product = 1
            for index, val in enumerate(aList):
                if index != idx:
                    product *= val
            new_list.append(product)
        return new_list
    except (TypeError, ValueError, NameError):
        print("Oops! Please check your input value")


# test the function
test_list = [1, 2, 3, 4, 5]
print(f'>>> New list for input: {test_list} is: {problem_2(test_list)} <<<')
