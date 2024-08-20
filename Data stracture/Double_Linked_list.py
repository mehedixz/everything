class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self,val):
        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def remove_last(self):
        self.tail = self.tail.prev
        self.tail.next = None
        return self.head

    def __str__(self):
        list = []
        curr = self.head
        while curr:
            list.append(curr.data)
            curr = curr.next

        return str(list)

# llist = Linked_list()
# llist.insert(5)
# llist.insert(4)
# llist.insert(56)
# llist.insert(532)
# llist.insert(845)
# print(llist)
