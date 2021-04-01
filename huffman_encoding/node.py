class Node:
    def __init__(self, frequency, char=None):
        self.char = char
        self.frequency = frequency
        self.left_node = None
        self.right_node = None
        self.huffman_code = ''

    def get_frequency(self):
        return self.frequency

    def get_char(self):
        return self.char

    def set_left_node(self, node):
        self.left_node = node

    def set_right_node(self, node):
        self.right_node = node

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def has_left_node(self):
        return self.left_node is not None

    def has_right_node(self):
        return self.right_node is not None

    def is_leaf_node(self):
        return self.right_node is None and self.left_node is None

    # operators overload to make heap priority queue work
    def __gt__(self, other):
        return (self.frequency > other.frequency)

    def __lt__(self, other):
        return (self.frequency < other.frequency)

    def __eq__(self, other):
        return (self.frequency == other.frequency)
