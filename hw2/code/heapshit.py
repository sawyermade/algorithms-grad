# def heapsort(A):
# 	buildMaxHeap(A)
# 	for i in range(len(A)-1, 0, -1):
# 		A[i], A[0] = A[0], A[i]
# 		maxHeapify(A, 0)

# def buildMaxHeap(A):
# 	for i in range(len(A)//2, -1, -1):
# 		maxHeapify(A, i)

# def maxHeapify(A, i):
# 	l = 2*i + 1
# 	r = 2*i + 2
# 	n = len(A)

# 	largest = i

# 	if l < n and A[i] < A[l]:
# 		largest = l

# 	if r < n and A[largest] < A[r]:
# 		largest = r

# 	if largest != i:
# 		A[i], A[largest] = A[largest], A[i]
# 		maxHeapify(A, largest)

# def main():
# 	# A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
# 	A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
# 	buildMaxHeap(A)
# 	# heapsort(A)
# 	print(A)

# if __name__ == '__main__':
# 	main()


# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    print(arr)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
 
# Driver code to test above
arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
heapSort(arr)
n = len(arr)

# This code is contributed by Mohit Kumra