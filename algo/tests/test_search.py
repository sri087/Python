import sys
sys.path.append('..')

from src.searches import binary_search

small_list = [2.5,1,4,6]
big_list = [2.5,5.5,3,6,5,1,-10,56,34,26]

odd_big_list = big_list + [72]

def test_search_small_list():

    assert binary_search([], 4) == False
    assert binary_search([4], 4) == True
    assert binary_search(small_list, 4) == True
    assert binary_search(small_list, 7) == False
    assert binary_search(small_list, 2.5) == True
    assert binary_search(small_list, 6) == True
    assert binary_search(small_list, 1) == True

def test_search_big_list():

    assert binary_search(big_list, -10) == True
    assert binary_search(big_list, 56) == True
    assert binary_search(big_list, 7) == False

def test_search_odd_big_list():

    assert binary_search(odd_big_list, -10) == True
    assert binary_search(odd_big_list, 56) == True
    assert binary_search(odd_big_list, 5.5) == True
    assert binary_search(odd_big_list, 7) == False
    assert binary_search(odd_big_list, 72) == True
    

