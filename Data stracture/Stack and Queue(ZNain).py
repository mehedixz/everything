from Double_Linked_list import Linked_list


class Stack:
    def __init__(self):
        self.list = Linked_list()

    def push(self, value):
        self.list.insert(value)

    def pop(self):
        self.list.remove_last()

    def peek(self):
        print("peek data is : ",self.list.tail.data)

    def is_empty(self):
        if self.list.size == 0:
            print("empty")
        else:
            print("not empty")

    def __str__(self):
        list = []
        curr = self.list.head
        while curr:
            list.append(curr.data)
            curr = curr.next
        return str(list)


stack = Stack()
stack.push(5)
stack.push(8)
stack.push(13)
stack.push(4)
stack.push(9)
stack.peek()
stack.pop()
stack.is_empty()
print(stack)
