class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class Link_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,val):
        node = Node(val)

        if self.head is None:
            self.head = node
            self.size += 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def __str__(self):
        list = []
        curr = self.head
        while curr:
            list.append(curr.data)
            curr = curr.next

        return str(list)

llist = Link_list()
llist.insert(5)
llist.insert(4)
llist.insert(6)
llist.insert(45)
llist.insert(55)
llist.insert(57)
llist.insert(59)
llist.insert(53)
llist.insert(54)
print(llist)
print(llist.size)
