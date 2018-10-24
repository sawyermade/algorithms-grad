import random, time

# Swaps i and j
def exchange(A, i, j):
	A[i], A[j] = A[j], A[i]

# Partitions array
def partition(A, p, r):
	x = A[r]
	i = p-1

	for j in range(p, r):
		if A[j] <= x:
			i += 1
			exchange(A, i, j)

	exchange(A, i+1, r)
	return i+1

# Sorts
def quickSort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quickSort(A, p, q-1)
		quickSort(A, q+1, r)

if __name__ == '__main__':
	# Sets up random
	random.seed(time.time())

	# Arrays to sort
	A1 = [random.randint(0, 100) for i in range(100)]
	A2 = [i for i in range(100)]
	A3 = [i for i in range(99, -1 , -1)]
	
	# Sorts arrays
	quickSort(A1, 0, len(A1) - 1)
	quickSort(A2, 0, len(A2) - 1)
	quickSort(A3, 0, len(A3) - 1)

	# Prints
	print(A1)
	print(A2)
	print(A3)