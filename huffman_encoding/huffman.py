import heapq
from node import Node
from tree import Tree


def huffman_encoding(data):
    if not data:
        return None, None

    def create_priority_queue(frequency_dict):

        heap_priority_queue = []

        for char, frequency in frequency_dict.items():

            node = Node(frequency, char)
            heapq.heappush(heap_priority_queue, node)

        return heap_priority_queue

    def get_char_frequency_dict(data):

        frequency_dict = {}

        for char in data:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

        return frequency_dict

    def traverse_tree(node, encoded_data_dict={}):
        if node.is_leaf_node():
            char = node.get_char()
            encoded_data_dict[char] = node.huffman_code
            return encoded_data_dict

        if node.has_left_node():
            left_node_huffman_code = node.get_left_node().huffman_code
            node.get_left_node().huffman_code = node.huffman_code + left_node_huffman_code
            traverse_tree(node.get_left_node(), encoded_data_dict)

        if node.has_right_node():
            right_node_huffman_code = node.get_right_node().huffman_code
            node.get_right_node().huffman_code = node.huffman_code + right_node_huffman_code

            traverse_tree(node.get_right_node(), encoded_data_dict)

        return encoded_data_dict

    frequency_dict = get_char_frequency_dict(data)
    priority_queue = create_priority_queue(frequency_dict)

    tree = Tree()

    if len(priority_queue) == 1:
        node = heapq.heappop(priority_queue)
        tree.set_root(node)

        frequency = node.get_frequency()

        encoded_data = ''
        for i in range(0, frequency + 1):
            encoded_data += '1'

        return encoded_data, tree

    # pop lowest two nodes and make a combined node out of them
    # till one node is left in the priority queue which is going to be the root node
    while len(priority_queue) > 1:

        first_node = heapq.heappop(priority_queue)
        second_node = heapq.heappop(priority_queue)

        new_frequency = first_node.get_frequency() + second_node.get_frequency()
        new_node = Node(new_frequency)

        lower_frequency_node = first_node
        higher_frequency_node = second_node

        if first_node > second_node:
            lower_frequency_node = second_node
            higher_frequency_node = first_node

        lower_frequency_node.huffman_code = '0'
        higher_frequency_node.huffman_code = '1'

        new_node.set_left_node(lower_frequency_node)
        new_node.set_right_node(higher_frequency_node)

        heapq.heappush(priority_queue, new_node)

    root_node = heapq.heappop(priority_queue)
    tree.set_root(root_node)

    # traverse the tree to get code

    encoded_data_dict = traverse_tree(root_node)

    print(encoded_data_dict)

    encoded_data = ''
    for char in data:
        encoded_data += encoded_data_dict[char]

    return encoded_data, tree


def huffman_decoding(data, tree):

    if not data or not tree:
        return None

    def decode_traversed_tree(node, data, index, decoded_string=""):

        if node.is_leaf_node():
            return index, node.get_char()

        elif data[index] == "0":
            node_to_traverse = node.get_left_node()

        elif data[index] == "1":
            node_to_traverse = node.get_right_node()

        return decode_traversed_tree(node_to_traverse, data, index + 1, decoded_string)

    index = 0
    decoded_data = ""

    while(index <= len(data) - 1):
        index, decoded_string = decode_traversed_tree(
            tree.get_root(), data, index)

        decoded_data += decoded_string

    return decoded_data
