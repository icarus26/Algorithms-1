# Python program for implementation of Merge Sort
# l is left index, m is middle index and r is right index
# L[l...m] and R[m+1.....r] are respective left and right sub-arrays


def merge(arr, l, m, r):
		n1 = m - l + 1
		n2 = r-m

	#create temporary arrays
	
	L = [0]*(n1)
	R = [0]*(n2)

	#Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m+1+j]

	# Merge the temp array back into arr[l...r]
	
	i = 0 	# Initial index of first subarray
	j = 0 	# Initial index of second subarray
	k = l 	# Initial index of merged subarray

#Comparing the elements of the array and filling them into one array
	
	while i < n1 and j < n2 :
		if L[i] <= R[j] :
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining element of L[], if there are any

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy  the remaining element of R[], if there are any

	while j < n2:
		arr[k] R[j]
		j += 1
		k += 1

	# l is for left index and r is for right index of the 
	# subarray of arr to be sorted

	def mergeSort(arr, l, r):
		if l < r:

			#Same as (l+r)/2, but avoid overflow for large l and h

			m = (l+(r-1))/2
			# Sort first and second halves
			mergeSort(arr, l, m)
			mergeSort(arr, m+1, r)
			merge(arr, l, m, r)


