from linkedlist import LinkedList


def union(linked_list_1, linked_list_2):
    if not linked_list_1.head and not linked_list_2.head:
        raise ValueError("One of the two lists should have values")

    unique_combined_values = set()

    union_list = LinkedList()

    linked_list_1_unique_values = linked_list_1.add_nodes_to_set(
        unique_combined_values)

    linked_list_2_unique_values = linked_list_2.add_nodes_to_set(
        unique_combined_values)

    for value in unique_combined_values:
        union_list.append(value)

    return union_list


def intersection(linked_list_1, linked_list_2):

    if not linked_list_1.head and not linked_list_2.head:
        raise ValueError("One of the two lists should have values")

    unique_values_1 = set()
    linked_list_1_unique_values = linked_list_1.add_nodes_to_set(
        unique_values_1)

    unique_values_2 = set()

    linked_list_2_unique_values = linked_list_2.add_nodes_to_set(
        unique_values_2)

    common_values = unique_values_1.intersection(unique_values_2)

    intersection_list = LinkedList()

    for value in common_values:
        intersection_list.append(value)

    return intersection_list
