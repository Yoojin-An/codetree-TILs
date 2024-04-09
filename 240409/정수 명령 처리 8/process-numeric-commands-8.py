class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        
        self.node_num += 1
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):
        if self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            print(temp.data)
      
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1
            print(temp.data)

    def pop_back(self):
        if self.tail.prev == None:
            temp = self.tail
            self.head = None
            self.tail = None
            self.node_num = 0
            print(temp.data)

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1
            print(temp.data)
    
    def size(self):
        print(self.node_num)
    
    def empty(self):
        if self.node_num:
            print(0)
        else:
            print(1)
    
    def front(self):
        print(self.head.data)

    def back(self):
        print(self.tail.data)


l = Doubly_linked_list()
N = int(input())
for _ in range(N):
    command = input()
    if command.startswith("push_front"):
        command, param = command.split()
        l.push_front(int(param))
    elif command.startswith("push_back"):
        command, param = command.split()
        l.push_back(int(param))
    elif command == "pop_front":
        l.pop_front()
    elif command == "pop_back":
        l.pop_back()
    elif command == "size":
        l.size()
    elif command == "empty":
        l.empty()
    elif command == "front":
        l.front()
    elif command == "back":
        l.back()