import random, time

comps = 0

# Swaps i and j
def exchange(A, i, j):
	A[i], A[j] = A[j], A[i]

def randPart(A, p, r):
	global comps
	comps += 1

	i = random.randint(p, r)
	exchange(A, i, r)
	return partition(A, p, r)

# Partitions array
def partition(A, p, r):
	global comps
	x = A[r]
	i = p-1

	for j in range(p, r):
		comps += 1
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

def randQuickSort(A, p, r):
	global comps
	comps += 1
	if p < r:
		q = randPart(A, p, r)
		randQuickSort(A, p, q-1)
		randQuickSort(A, q+1, r)

if __name__ == '__main__':
	# Sets up random
	random.seed(time.time())

	# Arrays to sort
	A1 = [random.randint(0, 100) for i in range(100)]
	A2 = [i for i in range(100)]
	A3 = [i for i in range(99, -1 , -1)]
	A4 = [100] * 100
	
	# Sorts arrays
	# quickSort(A1, 0, len(A1) - 1)
	# quickSort(A2, 0, len(A2) - 1)
	# quickSort(A3, 0, len(A3) - 1)
	comps = 0
	randQuickSort(A1, 0, len(A1) - 1)
	print(comps)
	comps = 0
	randQuickSort(A2, 0, len(A2) - 1)
	print(comps)
	comps = 0
	randQuickSort(A3, 0, len(A3) - 1)
	print(comps)
	comps = 0
	randQuickSort(A4, 0, len(A4) - 1)
	print(comps)
	comps = 0

	# Prints
	print(A1)
	print(A2)
	print(A3)