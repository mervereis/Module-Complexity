from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")

def find_common_items(
    first_sequence: Sequence[ItemType],
    second_sequence: Sequence[ItemType]
) -> List[ItemType]:

    second_set = set(second_sequence)
    common_items = []
    seen = set()

    for item in first_sequence:
        if item in second_set and item not in seen:
            common_items.append(item)
            seen.add(item)

    return common_items


print(find_common_items([1, 2, 3, 4], [2, 3, 5]))
# [2, 3]

"""
Find common items between two arrays.

Time Complexity: O(n * m * k)
Space Complexity: O(k)
Optimal Time Complexity: O(n + m)
"""