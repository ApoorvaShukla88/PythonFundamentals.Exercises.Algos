from math import ceil
from math import floor
from typing import List


def binary_search(list_in: List[int], item: int) -> int:
    sorted_list = sorted(list_in)

    #print(len(list_in))
    first = 0
    last = len(list_in) - 1

    #print(mid)

    while first <= last:
        mid = round((first + last) // 2)

        if sorted_list[mid] == item:
            return list_in.index(item)

        elif sorted_list[mid] < item:
            first = mid + 1
            mid = round((first + last) / 2)
        elif sorted_list[mid] > item:
            last = mid
            mid = round(mid/2)

    return -1


if __name__ == "__main__":
    result = binary_search([15, 12, 54, 16, 9, 10, 2, 65, 33, 77, 99, 23, 29, 18, ], 54)

    print(result)



