# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(smallest_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        lowest = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = lowest

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True

    while swap:
        swap = False
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
    
test_list1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
test_list2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort(test_list1))
print(bubble_sort(test_list2))