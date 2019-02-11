"""
@author: Okwudili Ezeme
@date: 2019-01-14
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

islocked, which returns whether the node is locked
lock_node, which attempts to lock_node the node. If it cannot be locked, then it should return false. Otherwise, it should lock_node it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""


class BinaryTree():
    def __init__(self, value, lock_node=False):
        self.locked = lock_node
        self.value = value
        self.left = None
        self.right = None

    def lock_node(self):
        """lock_node a node if the descendants are locked using post-order traversing"""
        return self.locked and all(node.lock_node() for node in (self.left, self.right) if node)

    def unlock(self, node):
        """unlock if ancestors are unlocked. We assume that Tree stores numbers"""
        if self.value == None:  # empty tree
            print(f'>>> Node: {node} not found <<<')
            return False  # empty Binary Tree
        elif node < self.value and self.left:
            if self.locked == True:
                print(
                    f'>>> Ancestor: {self.value} is locked. unlock failed <<<')
                return False
            else:
                print(
                    f'>>> Ancestor: {self.value} \tstatus: {self.locked} <<<')
                return self.left.unlock(node)
        elif node > self.value and self.right:
            if self.locked == True:
                print(
                    f'>>> Ancestor: {self.value} is locked. unlock failed <<<')
                return False
            else:
                print(
                    f'>>> Ancestor: {self.value} \tstatus: {self.locked} <<<')
                return self.right.unlock(node)
        elif self.value == node:
            self.locked = True
            print(f'Node: {node} successfully unlocked <<<')
            return True

    def add_node(self, value, lock_node=False):
        """add a node to the tree with lock_node value"""
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.add_node(value, lock_node)
                else:
                    self.left = BinaryTree(value, lock_node)
            elif value >= self.value:
                if self.right:
                    self.right.add_node(value, lock_node)
                else:
                    self.right = BinaryTree(value, lock_node)
        else:
            self.value = value
            self.locked = lock_node

    def find_node(self, node):
        """return the node object given by the key `node` in the arguments"""
        if self.value == None:
            print(f'>>> Node: {node} not found <<<')
            return False
        elif node < self.value and self.left:
            return self.left.find_node(node)
        elif node > self.value and self.right:
            return self.right.find_node(node)
        elif self.value == node:
            return self
        else:
            print(f'>>> Node: {node} not found <<<')
            return False

    def set_lock(self, node, lock_node):
        """set the lock_node of a particular node to False or True to aid testing"""
        if self.value == None:  # empty tree
            print(f'>>> Node: {node} not found <<<')
            return False  # empty Binary Tree
        elif node < self.value and self.left:
            return self.left.set_lock(node, lock_node)
        elif node > self.value and self.right:
            return self.right.set_lock(node, lock_node)
        elif self.value == node:
            prev_state = self.locked
            self.locked = lock_node
            new_state = self.locked
            print(
                f'>>> Node {self.value} lock changed from: {prev_state} ---> {new_state} <<<')
            return True

        # test the functions
if __name__ == "__main__":
    BT = BinaryTree(None)
    count = 0
    lock_state = False
    nodes = [34, 2, 1, 6, 8, 9, 56, 99, 150, 45, 3]
    for item in nodes:
        BT.add_node(item, lock_state)  # test add_node
    BT.set_lock(45, True)
    BT.set_lock(99, True)
    BT.set_lock(150, True)
    BT.unlock(6)  # test unlock
    node = BT.find_node(56)
    result = all(child.lock_node()
                 for child in (node.left, node.right) if child)
    print(result)
    if result:
        BT.set_lock(node.value, True)
