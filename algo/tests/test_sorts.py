import sys

from numpy import true_divide
sys.path.append('..')

from src.sorts import bubble_sort, insertion_sort
from src.searches import binary_search

class TestSorts():

    small_list = [2.5,1,4,6,2.5]
    big_list = [2.5,5.5,3,6,5,1,-10,56,34,26,26]

    odd_big_list = big_list + [72]

    def _compare(self, a_list, b_list):

        

        if len(a_list) != len(b_list):
            return False

        for x,y in zip(a_list,b_list):
            if x != y: return False
        
        return True


    def test_bubble_sort(self):

        assert self._compare(bubble_sort(self.small_list),sorted(self.small_list)) == True
        assert self._compare(bubble_sort(self.small_list,ascending=False),sorted(self.small_list,reverse=True)) == True
        assert self._compare(bubble_sort(self.big_list),sorted(self.big_list)) == True
        assert self._compare(bubble_sort(self.big_list,ascending=False),sorted(self.big_list,reverse=True)) == True

    def test_insertion_sort(self):

        assert self._compare(insertion_sort(self.small_list),sorted(self.small_list)) == True
        assert self._compare(insertion_sort(self.small_list,ascending=False),sorted(self.small_list,reverse=True)) == True
        assert self._compare(insertion_sort(self.big_list),sorted(self.big_list)) == True
        assert self._compare(insertion_sort(self.big_list,ascending=False),sorted(self.big_list,reverse=True)) == True

    def test_search_odd_big_list(self):

        assert binary_search(self.odd_big_list, -10) == True
        assert binary_search(self.odd_big_list, 56) == True
        assert binary_search(self.odd_big_list, 5.5) == True
        assert binary_search(self.odd_big_list, 7) == False
        assert binary_search(self.odd_big_list, 72) == True
    

