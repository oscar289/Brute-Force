def brute_force(target, possibilities):
    """
    Attempt to find the target value by trying every possibility in the list of possibilities.

    Parameters:
    - target (any): The value that we are trying to find.
    - possibilities (list): A list of potential values that could be the target.

    Returns:
    - The target value if it is found in the list of possibilities, or None if it is not found.
    """
    for x in possibilities:
        if x == target:
            return target  # "The target value if it is found"

    return None  # None if it is not found.


print(brute_force(1, [1, 2, 3, 4, 5, 6, 7]))
print(brute_force(8, [1, 2, 3, 4, 5, 6, 7]))
