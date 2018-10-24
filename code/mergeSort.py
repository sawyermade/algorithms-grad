import sys

def mergeSort(A, start, stop):
	if start < stop:
		mid = (start+stop) // 2
		mergeSort(A, start, mid)
		mergeSort(A, mid+1, stop)
		merge(A, start, mid, stop)

def merge(A, start, mid, stop):
	n1 = mid - start + 1
	n2 = stop - mid

	L, R = [], []

	for i in range(1, n1+1):
		L.append(A[start + i - 1])
	for j in range(1, n2+1):
		R.append(A[mid + j])

	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i, j = 0, 0

	for k in range(start, stop+1):
		if L[i] < R[j]:
			A[k] = L[i]
			i += 1

		else:
			A[k] = R[j]
			j += 1

def main():
	# Arrays to heapify/sort/priority queue
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    B = [5, 13, 2, 25, 7, 17, 20, 8, 4]

    # Merge sort
    mergeSort(A, 0 , len(A)-1)
    print(A)

if __name__ == '__main__':
	main()