"""
@author: Okwudili Ezeme
@date: 2019-02-23
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""


def print_matrix(matrix):
    while matrix:
        # go right
        if matrix:
            for index in range(len(matrix[0])):
                print(f'>>> {matrix[0].pop(0)}')
            matrix = matrix[1:]
        # go down
        if matrix:
            for row_id in range(len(matrix)):
                print(f'>>> {matrix[row_id].pop()}')
        # go left
        if matrix:
            for index in range(len(matrix[0])):
                print(f'>>> {matrix[-1].pop()}')
            matrix = matrix[:-1]
        # go up
        if matrix:
            for row_id in range(len(matrix)):
                index = -1 * (row_id + 1)
                print(f'>>> {matrix[index].pop(0)}')


# test the function
if __name__ == "__main__":
    matrix = [[1,  2,  3,  4,  5],
              [6,  7,  8,  9,  10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]]
    print_matrix(matrix)
