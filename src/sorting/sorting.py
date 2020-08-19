import math

def merge(arrA, arrB):

    #adjusted the original variables

    merged_arr = []

    # MARK: counts
    left_count = len(arrA)
    right_count = len(arrB)
    left_i, right_i = 0, 0  

    # fill the merged_arr with sorted values, checking both arrays until one of them has been
    # completely processed
    print(f"array A: {arrA}")
    print(f"array B: {arrB}")

    while left_i < left_count and right_i < right_count:
        if arrA[left_i] < arrB[right_i]:
            merged_arr.append(arrA[left_i])
            print(f"left: {arrA[left_i]}")
            left_i += 1            
        elif arrA[left_i] == arrB[right_i]:
            left_i += 1
            right_i += 1
            merged_arr.append(arrA[left_i])
            merged_arr.append(arrB[right_i])
            print(f"both: {arrB[right_i]}")
        else:
            print(f"right: {arrB[right_i]}")
            merged_arr.append(arrB[right_i])
            right_i += 1            
    # fill any remaining elements since the above loop will end when either array is processed - then return the result    
    merged_arr += arrA[left_i:]
    merged_arr += arrB[right_i:]
    print(f"merged: {merged_arr}\n")
    return merged_arr
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    # base case
    if len(arr) <= 1:

        return arr

    # find the midpoint
    mid = len(arr)//2

    # split and recursively sort and merge the result
    left =  merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
        
    return merge(left, right)

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(f"final: {merge_sort(arr1)}")

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass



