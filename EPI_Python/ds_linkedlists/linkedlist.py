"""
Implementation of linked list, and some util methods to construct and print them
Note: this class def is pythonic and follows https://realpython.com/linked-lists-python/ 
"""
from __future__ import annotations
from typing import List, Any, Iterable

class LinkedNode:
    """List single node"""
    data: int
    next: LinkedNode

    def __init__(self, data: int=0, next_node: LinkedNode=None) -> None:
        """ Initialize the linked list node"""
        self.data = data
        self.next = next_node

    def __repr__(self):
        """Printable linked list node"""
        return self.data


class LinkedList:
    """A collection of LinkedNode-s"""
    head: LinkedNode

    def __init__(self, node_data: List[Any]=None) -> None:
        """ Initialize (also construct) the linked list """
        if not node_data:
            self.head = None
        else:
            new_node = LinkedNode(data=node_data.pop(0))
            self.head = new_node
            for datapoint in node_data:
                new_node.next = LinkedNode(data=datapoint)
                new_node = new_node.next
    
    def __repr__(self) -> str:
        """Printable linked list"""
        node = self.head
        node_data = []
        while node is not None:
            node_data.append(node.data)
            node = node.next
        node_data.append("None")
        return " -> ".join(node_data)

    def __iter__(self) -> Iterable[LinkedNode]:
        node = self.head
        while node is not None:
            yield node
            node = node.next


