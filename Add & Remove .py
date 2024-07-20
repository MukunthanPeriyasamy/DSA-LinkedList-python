class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


class LinkedList:
    def __init__(self):
        self.head = None

    #LinkedList add method
    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.pointer is not None:
                temp = temp.pointer
            temp.pointer = newNode

    #linkedlist remove method

    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.pointer
            else:
                temp = self.head
                while temp.pointer is not None and temp.pointer.data != data:
                    temp = temp.pointer
                if temp.pointer is not None:
                    temp.pointer = temp.pointer.pointer
                    print(data,"is removed from LinkedList")
                else:
                    print(data, " is not present in the linked List")
        else:
            print("Linked list is empty")

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            if temp.pointer is not None:
                print("-->", end=" ")
            temp = temp.pointer
        print()


ll = LinkedList()
ll.add("1")
ll.add("2")
ll.add("3")
ll.add("4")
ll.print()
ll.remove("6")
ll.print()
