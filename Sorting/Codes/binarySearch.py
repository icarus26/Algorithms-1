# Python Program for recursive binary search

# Returns index of x in arr if present, else -1

def binarySearch(arr, l, r, x):
    # check base case
    if r >= l:
        mid = (l + (r-1))/2

        # If the element is present at the middle itself

        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only 
        # be present in left sub-array
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present in right sub-array
    else: 
        return binarySearch(arr, mid+1, r, x)
    
    else:
        # Element is not present in the array
        return -1