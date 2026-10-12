def has_pair_with_sum(numbers, target_sum):

    seen = set()

    for number in numbers:
        complement = target_sum - number

        if complement in seen:
            return True

        seen.add(number)

    return False


print(has_pair_with_sum([2, 4, 6, 8], 10))
# True

print(has_pair_with_sum([1, 2, 3], 10))
# False
"""
Find if there is a pair of numbers that sum to a target value.

Time Complexity: O(n²)
Space Complexity: O(1)
Optimal Time Complexity: O(n)
"""