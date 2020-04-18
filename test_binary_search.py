import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        test_cases = [
            ([1, 3, 5, 7, 9, 11, 13], 9, 4),
            ([0, 2, 4, 6, 8, 10, 12, 14], 2, 1),
            ([77, 79, 81, 25, 45, 78], 81, 2),
            ([150, 152, 154, 156, 99, 100, 22, 65], 152, 1)

        ]

        for list_in, item, expected in test_cases:
            # result = binary_search(list_in, item)
            # self.assertEqual(result, expected)

            # with self.subTest(f"{list_in} {item} -> {expected}"):
            self.assertEqual(expected, binary_search(list_in, item))





