######################### 	 SORTING  	########################

import numpy as np 

# Bubble sort
def bubble(array):
	for i in range(len(array)):
		for j in range(len(array) - 1):
			if array[j] > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

		print(array)

arr = np.array([1,2,3,4,5])
# bubble(arr)

# Bubble sort with flag
def bubble_flag(array):
	swapped = True
	while swapped == True:
		swapped = False 
		for j in range(len(array) - 1):
			if array[j] > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
				swapped = True
		print(array)

	return array

print(bubble_flag(arr))