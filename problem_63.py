"""
@author: Okwudili Ezeme
@date: 2019-02-21
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target pattern, write a function that returns whether the pattern can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target pattern 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target pattern 'MASS', you should return true, since it's the last row.
"""
import re


def check_row(matrix, target):
    # check the rows for the target pattern
    for row in matrix:
        pattern = ''
        for char in row:
            pattern = pattern + char
        if re.search(target, pattern, re.I):  # use search because target could be a substring
            return True
    return False


def check_column(matrix, target):
    # examine the columns for the target pattern
    num_col = len(matrix[0])  # get the number of columns
    pattern = ''
    index = 0
    while index < num_col:
        for row in matrix:
            pattern = pattern + row[index]
        if re.search(target, pattern, re.I):
            return True
        index += 1
        pattern = ''
    return False


def find_word(matrix, target):
    return any([check_column(matrix, target), check_row(matrix, target)])


if __name__ == "__main__":
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]
    targets = ['mass', 'foam', 'qos', 'ipob']
    for target in targets:
        print(f'>>> Found {target}?\t{find_word(matrix,target)}')
