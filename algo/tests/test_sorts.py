import sys

from numpy import true_divide
sys.path.append('..')

from src.sorts import bubble_sort
from src.searches import binary_search

class TestSorts():

    small_list = [2.5,1,4,6]
    big_list = [2.5,5.5,3,6,5,1,-10,56,34,26]

    odd_big_list = big_list + [72]

    def _compare(self, a_list, b_list):

        if len(a_list) != len(b_list):
            return False

        for x,y in zip(a_list,b_list):
            if x != y: return False
        
        return True


    def test_bubble_sort_small_list(self):

        assert self._compare(bubble_sort(self.small_list),sorted(self.small_list)) == True
        assert self._compare(bubble_sort(self.small_list,ascending=False),sorted(self.small_list,reverse=True)) == True
        assert binary_search(self.small_list, 4) == True
        assert binary_search(self.small_list, 7) == False
        assert binary_search(self.small_list, 2.5) == True
        assert binary_search(self.small_list, 6) == True
        assert binary_search(self.small_list, 1) == True

    def test_search_big_list(self):

        assert binary_search(self.big_list, -10) == True
        assert binary_search(self.big_list, 56) == True
        assert binary_search(self.big_list, 7) == False

    def test_search_odd_big_list(self):

        assert binary_search(self.odd_big_list, -10) == True
        assert binary_search(self.odd_big_list, 56) == True
        assert binary_search(self.odd_big_list, 5.5) == True
        assert binary_search(self.odd_big_list, 7) == False
        assert binary_search(self.odd_big_list, 72) == True
    

