# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
	# base
	if end < start:
		return -1 

	mid = (end + start) // 2 

	#got it
	if arr[mid] == target:
		return mid

	#target < mid, chekc left
	elif arr[mid] > target:
		return binary_search(arr, target, start, mid - 1)
	else:
		return binary_search(arr, target, mid + 1, end)

def descending_binary_search(arr, target, start, end):
    	# base
    if end < start:
    	return -1

    mid = (end + start) // 2

    # found 
    if arr[mid] == target: 
        return mid 

        # target smaller than mid, check right
    elif arr[mid] > target:
        return descending_binary_search(arr, target, mid + 1, end)
        # larger, check left
    else:
        return descending_binary_search(arr, target, start, mid - 1)            

# 
 
def agnostic_binary_search(arr, target):
    
    #check if descending
    descending = arr[0] > arr[1]
    if descending:
        return descending_binary_search(arr, target, 0, len(arr)-1)
    else:
        return binary_search(arr, target, 0, len(arr)-1)


arr1 = [-1,-2,-3,-4,-5,-6,-7]
arr2 = [-7,-6,-5,-4,-3,-2,-1]
result = agnostic_binary_search(arr2, -2)
print(result)