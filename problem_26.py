"""
@author: Okwudili Ezeme
@date: 2019-01-17
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node():
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class SinglyLinkedList():
    def __init__(self):
        self.node = None

    def find_node(self, node):
        current_node = self.node
        while current_node:
            if current_node.data == node:
                return current_node
            current_node = current_node.next_node
        return None

    def insert_at_start(self, node):
        # case 1: insert at the start of the list
        NewTerminal = Node(node)
        # make new node next_node pointer point to the start node
        if self.node:
            NewTerminal.next_node = self.node
            self.node = NewTerminal  # make new terminal the start node
        else:
            self.node = NewTerminal
        return

    def insert_at_middle(self, old_node, new_node):
        old_terminal = self.find_node(old_node)  # locate the node
        if old_terminal:
            NewTerminal = Node(new_node)
            NewTerminal.next_node = old_terminal.next_node
            old_terminal.next_node = NewTerminal
        else:
            print(f'>>> {old_node} not in the list <<<')
        return

    def insert_at_end(self, node):
        NewTerminal = Node(node)
        # base case: list is not empty
        if self.node:
            terminal_node = self.node
            while terminal_node:
                if terminal_node.next_node == None:
                    terminal_node.next_node = NewTerminal
                    break
                else:
                    terminal_node = terminal_node.next_node
        else:  # list is empty
            self.node = NewTerminal
        return

    def remove_node(self, integer_k):
        current_node = self.node
        counter = 1
        while current_node:
            if counter == integer_k:
                if current_node.next_node:  # it has a next node value
                    self.node = current_node.next_node
                    print(
                        f'>>> {current_node.data} with index {counter-1} removed <<<')
                    current_node = None
                    return
                else:
                    print(
                        f'>>> {current_node.data} with index {counter-1} removed <<<')
                    current_node = None  # last node with empty next node
                    return
            else:
                current_node = current_node.next_node
                counter += 1
        print(f'>>> {integer_k} is longer than the list length <<<')
        return


# test the algorithm
if __name__ == "__main__":
    SLL = SinglyLinkedList()
    SLL.insert_at_start('Mon')
    SLL.insert_at_end('Fri')
    SLL.insert_at_middle('Mon', 'Thur')
    SLL.remove_node(2)
