"""
@author: Okwudili Ezeme
@date: 2019-01-17
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def matched(string):
    stack = []  # list with stack behavior
    brackets = dict(zip('{[(', '}])'))
    for bracket in string:
        if bracket in brackets:
            stack.append(brackets[bracket])
        # check that the stack is not empty and whether the bracket matches the expected closing bracket
        elif not (stack and bracket == stack.pop()):
            return False
        elif bracket not in brackets.values():  # character not a valid bracket
            return False
    return not stack


# test the function
if __name__ == "__main__":
    matched_string = "([])[]({})"
    unmatched_string = "((()"
    print(matched(unmatched_string))
