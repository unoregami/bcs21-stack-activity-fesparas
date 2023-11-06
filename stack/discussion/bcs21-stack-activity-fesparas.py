class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DynamicStack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self, value):
        value = 
        new_node = node
        completed = self.head.value
        self.head = self.head.next
        self.size -= 1
        return completed

    def display(self):
        current = self.head
        while current:
            print(current.value, end = " | ")
            current = current.next
        print("End")
    

TaskManager = DynamicStack()
TaskManager.push("Cook: Cook Fish")
TaskManager.display()