####################### BINARY SEARCH #######################

import numpy as np

# Returns position of the value in the array
def binary_search(array,value):
	first = 0
	last = len(array) - 1
	while first <= last:
		mid = (first + last) // 2
		if array[mid] == value:
			return mid
		if array[mid] > value:
			last = mid - 1
		if array[mid] < value:
			first = mid + 1
	# If the value is not in the array
	return -1

### CHECK ###
array = np.array([1,2,3,4,5])
# Should print 4
print(binary_search(array,5))
# Should print -1
print(binary_search(array,6))