from typing import List


def binary_search(list_in: List[int], item: int) -> int:
    sorted_list = sorted(list_in)

    #print(len(list_in))
    first = 0
    last = len(list_in) - 1
    mid = round(len(list_in) / 2)
    #print(mid)

    while first <= last:

        if sorted_list[mid] < item:
            first = mid + 1
            mid = len(list_in) - round((mid+1)/2)
        elif sorted_list[mid] > item:
            last = mid - 1
            mid = round(mid/4)
        elif sorted_list[mid] == item:
            return list_in.index(item)

if __name__ == "__main__":
    result = binary_search([77, 79, 81, 25, 45, 78], 25)

    print(result)



