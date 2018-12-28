"""
@author: Okwudili Ezeme
@question:
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
    """


def problem_1(aList, k):
    try:
        # find the complement of the original list with respect to k
        complement_set = set([k - aList[idx] for idx in range(len(aList))])
        # create a set of the original list
        original_list_set = set(aList)
        if complement_set.isdisjoint(original_list_set):
            return False
        else:
            return True
    except (TypeError, ValueError):
        print("Oops! Please pass a list as an argument")


# Test the function
print(problem_1([34, 45, 12, 5, 67, 4, 5, 9], 100))
