empty = lambda x: len(x) == 0
def binary_search(elems: list, search_for) -> bool:
   
    if empty(elems):
        return False
    
    elems = sorted(elems)

    left = 0
    right = len(elems) - 1

    while left <= right:
        mid = (left + right) // 2

        if elems[mid] == search_for:
            return True
        elif search_for > elems[mid]:
            left = mid + 1
        elif search_for < elems[mid]:
            right = mid - 1

    return False


def main():
    assert binary_search([], 4) == False
    assert binary_search([2.5,1,4,6], 4) == True

if __name__ == '__main__':
    main()