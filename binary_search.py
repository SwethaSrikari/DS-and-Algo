########################### BINARY SEARCH ###########################

import numpy as np

def binary_search(array,value):
	"""
	Returns position of a value in the array (if it's in the array)
	using a while loop

	:params array: Array
	:params value: The element to be searched in the array
	"""
	first = 0 # index of first element
	last = len(array) - 1 # index of last element
	mid = (first + last) // 2 # index of the middle element
	while first <= last:		
		if array[mid] == value:
			return mid # Returns the index of the "value"
		elif array[mid] > value:
			last = mid - 1
			mid = (first + last) // 2
		elif array[mid] < value:
			first = mid + 1
			mid = (first + last) // 2
	# If the value is not in the array
	return -1

### CHECK ###
print("Using while loop")
array = np.array([1,2,4,5,6])
# Should print 3
print(binary_search(array,5))
# Should print 4
print(binary_search(array,6))
# Should print 1
print(binary_search(array,2))



##################### BINARY SEARCH (RECURSIVE) #####################
def binary_search_rec(array, value):
	"""
	Returns position of a value in the array (if it's in the array)
	using recursive method

	:params array: Array
	:params value: The element to be searched in the array
	"""
	first, last = 0, len(array) - 1 # index of first and last element
	def recursive(array, first, last):
		if first > last:
			return -1 # Value not in the array
		mid = (first + last) // 2 # index of the middle element
		if array[mid] == value:
			return mid
		elif array[mid] > value:
			return recursive(array, first, mid-1)
		elif array[mid] < value:
			return recursive(array, mid+1, last)

	return recursive(array, first, last)

### CHECK ###
print("Using recursion")
array = np.array([1,2,4,5,6])
# Should print 0
print(binary_search(array,1))
# Should print 4
print(binary_search(array,6))
# Should print 1
print(binary_search(array,2))
# Best case, should print 2
print(binary_search(array,4))
# Worst case, should print -1
print(binary_search(array,-2))


