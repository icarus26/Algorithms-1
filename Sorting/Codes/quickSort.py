# Python program for implementing Quick Sort
'''
	This function takes last element as pivot,
	places the pivot element as its correct position
	in sorted array, and places all the smaller
	(smaller than pivot) to left of pivot and all 
	greater elements to right of pivot
'''

def partition(arr, low, high):
	i = (low -1) 			# index of smaller element
	pivot = arr[high]	 	# pivot

	for j in range(low, high):

		# if current element is smaller than or equal to pivot
		if arr[j] <= pivot:
			#increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

'''
	The main function that implements QuickSort
	arr[] ---> Array to be sorted,
	low ---> Starting index,
	high ---> Ending index 
'''


def quickSort(arr, low, high):
	if low < high:

		# pi is the partition index,
		# arr[p] is now at right place
		pi = partition(arr, low, high)

		# Seperately sort elements before
		# partition and after partition

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)