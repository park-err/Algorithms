  def combine_sorted_lists(list_one, list_two):
    list_one_index = 0
    list_two_index = 0
    merged_list = []

    # Both lists have some items left in them.
    while list_one_index < len(list_one) and list_two_index < len(list_two):
        # Choose the smaller of the two items and add it to the
        # merged list.
        if list_one[list_one_index] <= list_two[list_two_index]:
            merged_list.append(list_one[list_one_index])
            list_one_index += 1
        else:
            merged_list.append(list_two[list_two_index])
            list_two_index += 1

    # Grab any lingering items in the first list after we've
    # exhausted the second list
    while list_one_index < len(list_one):
        merged_list.append(list_one[list_one_index])
        list_one_index += 1

    # Grab any lingering items in the second list after we've
    # exhausted the first list
    while list_two_index < len(list_two):
        merged_list.append(list_two[list_two_index])
        list_two_index += 1

    return merged_list

def merge_sort(the_list):

    # Base case: single element list
    if len(the_list) <= 1:
        return the_list

    # Split the input in half
    middle_index = len(the_list) / 2
    left  = the_list[:middle_index]
    right = the_list[middle_index:]

    # Sort each half
    left_sorted  = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves
    return combine_sorted_lists(left_sorted, right_sorted)