""""
Kahyberth Stiven Gonzalez
25 de junio del 2023
Lista simple

"""
from LinkedList.Node.node import Node


class SimplyList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        current = self.head
        before = None

        if current is None:
            self.head = node
        else:
            while current is not None and current.value < value:
                before = current
                current = current.tpnext

            if before is None:
                node.tpnext = self.head
                self.head = node
            else:
                node.tpnext = current
                before.tpnext = node

    def getIndex(self, i):
        counter = 0
        current = self.head
        while counter < i and current is not None:
            current = current.tpnext
            counter += 1
        if current is None:
            raise OverflowError

        return current.value

    def delete(self, v):
        current = self.head
        counter = 0
        before = None
        while current is not None and current.value != v:
            current = current.tpnext

        if current is None:
            raise ReferenceError

        if before is None:
          self.head = current.tpnext
        else:
            before.tpnext = current.tpnext

    def printValues(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.tpnext

    def length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.tpnext
        return length