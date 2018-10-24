def insertionSort(A):
	for j in range(1, len(A)):
		val = A[j]
		i = j-1

		while i >= 0 and A[i] > val:
			A[i+1] = A[i]
			i -= 1

		A[i+1] = val

def main():
	# Arrays to heapify/sort/priority queue
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    B = [5, 13, 2, 25, 7, 17, 20, 8, 4]

    # Insertion Sorting
    insertionSort(A)
    insertionSort(B)
    print(A)
    print(B)

if __name__ == '__main__':
	main()