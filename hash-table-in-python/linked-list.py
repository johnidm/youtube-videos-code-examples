from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node[T] = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Node[T] = None

    def insert(self, data: T):
        node = Node[T](data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def reverse(self):
        if self.head:
            privious: Node[T] = None

            while self.head is not None:
                next: Node[T] = self.head.next
                self.head.next = privious
                privious = self.head
                self.head = next

            self.head = privious

    def find_middle_node(self) -> Node[T]:
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l):
        current: Node[T] = l.head
        while current.next:
            current = current.next

        current.next = self.head
        self.head = l.head

    def traverse(self):
        current: Node[T] = self.head
        while current is not None:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    ll = LinkedList[int]()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    # ll.traverse()
    # print("-------")
    # ll.reverse()
    # ll.traverse()
    # print("Middle")
    # print(ll.find_middle_node().data)
    l2 = LinkedList[int]()
    l2.insert(10)
    l2.insert(11)
    l2.insert(12)

    ll.merge(l2)
    ll.reverse()
    ll.traverse()