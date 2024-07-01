import unittest
def selectionsort(array):
    length=len(array)
    for i in range(length-1):
        smallest=i
        for j in range(i+1,length):
            if(array[j] < array[smallest]):
                smallest=j
        array[smallest],array[i]=array[i],array[smallest]
    return array


class Testcases(unittest.TestCase):
    def test_selection(self):
        array=[7,6,8,9,2,6,9,10]
        self.assertListEqual([2, 6, 6, 7, 8, 9, 9, 10],selectionsort(array))


if __name__ == '__main__':
    unittest.main()
