class Node:
    def __init__(self, content):
        self.content = content
        self.next = None


class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_rear(self, new):
        new_node = Node(new)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print_list(self):
        q = self.front
        while q is not None:
            print(q.content)
            print(q.next)
            print("-----")
            q = q.next


# YOUR SENTENCE
my_str = "The greatest scientist is Nikola Tesla"
words = my_str.split()

word_lengths = LinkedList()

for word in words:
    word_lengths.add_rear(len(word))

word_lengths.print_list()