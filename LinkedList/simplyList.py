""""
Kahyberth Stiven Gonzalez
25 de junio del 2023
Lista simple

"""
from LinkedList.Node.node import Node


class SimplyList:

    def __init__(self):
        self.head = None

    def insert(self, value, name=None):

        if name is not None:
            node = Node(name, value)
        else:
            node = Node(None, value)

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

    def getindex(self, i):
        counter = 0
        current = self.head
        while counter < i and current is not None:
            current = current.tpnext
            counter += 1
        if current is None:
            raise OverflowError

        return current.value

    def delete(self, name):
        current = self.head
        before = None

        while current is not None and current.name != name:
            before = current
            current = current.tpnext

        if current is None:
            raise ReferenceError

        if before is None:
            self.head = current.tpnext
        else:
            before.tpnext = current.tpnext

    def printvalues(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.tpnext

    def printnames(self, name='Nombre', valor='Valor'):
        current = self.head
        while current is not None:
            print(f"{name} : {current.name}  {valor} : {current.value} ")
            current = current.tpnext


    @property
    def length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.tpnext
        return length

    def get_value_by_name(self, name):
        current = self.head
        while current is not None:
            if name == current.name:
                return current.value
            current = current.tpnext

    def set_value_by_name(self, name, value):
        current = self.head
        while current is not None:
            if name == current.name:
                current.value = value
            current = current.tpnext

    def search_name(self, name):
        current = self.head
        state = False
        while current is not None:
            if name == current.name:
                state = True
            current = current.tpnext
        return state
