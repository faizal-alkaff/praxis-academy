import unittest
from sorting_method import *

class TestMethods(unittest.TestCase):

    def test_bubblesort(self):
        bbllist = [8, 11, 3, 22, 16]
        bubbleSort(bbllist)
        self.assertEqual(bbllist, [3, 8, 11, 16, 22])

    def test_quick_sort(self):
        quickSort = [22, 5, 1, 18, 99]
        quick_sort(quickSort)
        self.assertEqual(quickSort, [1, 5, 18, 22, 99])

    def test_insertion_sort(self):
        insertionSort = [9, 8, 19, 0, 34]
        insertion_sort(insertionSort)
        self.assertEqual(insertionSort, [0, 8, 9, 19, 34])

    def test_heap_sort(self):
        heapSort = [35, 12, 43, 8, 51]
        heap_sort(heapSort)
        self.assertEqual(heapSort, [8, 12, 35, 43, 51])

    def test_selection_sort(self):
        selectionSort = [12, 8, 3, 20, 11]
        selection_sort(selectionSort)
        self.assertEqual(selectionSort, [3, 8, 11, 12, 20])

if __name__ == '__main__':
    unittest.main()