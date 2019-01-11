"""
@author: Okwudili Ezeme
@date: 2018-12-30

This problem was asked by Google.

Given the value to a binary tree, implement serialize(value), which serializes the tree into a value, and deserialize(s), which deserializes the value back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('value', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def get_root(self):
        return self.value

    def find_value(self, value):
        if self.value:
            if self.value == value:
                print(f'>>> {self.value} found <<<')
                return
            if self.left_child:
                self.left_child.find_value(value)
            if self.right_child:
                self.right_child.find_value(value)



# test the tree
if __name__ == "__main__":
    import pickle
    node = Node('value', Node('left', Node('left.left')), Node('right'))
    assert pickle.loads(pickle.dumps(
        node)).left_child.left_child.value == 'left.left', 'Serialization failed'
