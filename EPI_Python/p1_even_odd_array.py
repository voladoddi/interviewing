"""
Re-order array entries such that even entries all appear first
"""
from typing import List


def is_odd(x: int) -> bool:
    """ check if input number is odd"""
    if x % 2 == 0:
        return False
    return True

def is_even(x: int) -> bool:
    """ check if input number is even"""
    if x % 2 == 0:
        return True
    return False

def even_odd(input_array: List[int]) -> None:
    """
    :param input_array: input array of integers to arrange into even numbers on one side,
                        odd on the other in-place
    """
    even_ptr = 0
    odd_ptr = len(input_array)-1

    while even_ptr < odd_ptr:
        if is_odd(input_array[odd_ptr]):
            odd_ptr -= 1
            print(f"odd ptr is at : {odd_ptr}")
        if is_even(input_array[even_ptr]):
            even_ptr += 1
            print(f"even ptr is at : {even_ptr}")
        elif is_odd(input_array[even_ptr]) and is_even(input_array[odd_ptr]):
            tmp = input_array[even_ptr]
            input_array[even_ptr] = input_array[odd_ptr]
            input_array[odd_ptr] = tmp
            even_ptr += 1
            odd_ptr -= 1
            print(f"odd ptr is at : {odd_ptr}")
            print(f"even ptr is at : {even_ptr}")

a = [1, 2, 3, 4, 5, 6, 8, 10, 13]
print(f"BEFORE: {a}")
even_odd(a)
print(f"AFTER: {a}")
