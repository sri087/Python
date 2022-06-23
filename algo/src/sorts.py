
def bubble_sort(to_sort:list, ascending:bool = True) -> list :

    list_length = len(to_sort)

    for i in range(0,list_length):
        for j in range(0,list_length-i-1):
            if ascending:
                if to_sort[j] > to_sort[j+1]:
                    to_sort[j],to_sort[j+1] = to_sort[j+1],to_sort[j]
            else:
                if to_sort[j] < to_sort[j+1]:
                    to_sort[j],to_sort[j+1] = to_sort[j+1],to_sort[j]
    return to_sort

def insertion_sort(to_sort:list, ascending:bool = True) -> list :

    list_length = len(to_sort)

    for i in range(1, list_length):
        current_item = to_sort[i]
        j = i - 1 

        while j >= 0:
            if ascending:
                if to_sort[j] > current_item:
                    to_swap = to_sort[j]
                    to_sort[j] = current_item
                    to_sort[j+1] = to_swap
            else:
                if to_sort[j] < current_item:
                    to_swap = to_sort[j]
                    to_sort[j] = current_item
                    to_sort[j+1] = to_swap
            j = j - 1

    return to_sort


def merge_sort(to_sort:list, ascending:bool = True) -> list :
    pass