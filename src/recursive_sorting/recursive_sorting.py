# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    left = 0
    right = 0
    total = 0

    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr[total] = arrA[left]
            left += 1
            total += 1
        else: 
            merged_arr[total] = arrB[right]
            right += 1
            total += 1
    while left < len(arrA):
        merged_arr[total] = arrA[left]
        left += 1
        total += 1
    while right < len(arrB):
        merged_arr[total] = arrB[right]
        right += 1
        total += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        return merge(merge_sort(left_arr), merge_sort(right_arr))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

test1 = [1, 3, 5, 7, 9]
test2 = [0, 2, 4, 6, 8]
test_list = [2, 1, 7, 4, 100, 0, 8, 5, 9, 33]
print(merge(test1, test2))
print(merge_sort(test_list))
