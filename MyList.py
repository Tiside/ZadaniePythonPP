from Node import Node
class MyList:
    def __init__(self):
        self.head = None


    def add_element(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            element = self.head
            while element.next is not None:
                element = element.next
            element.next = new_node

    def display(self):
        element = self.head
        while element is not None:
            print(element.value)
            element = element.next