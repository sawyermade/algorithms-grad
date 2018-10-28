import random, time

def countingSort(A, B, k):
	if len(A) > 1:
		C = []
		for i in range(0, k+1):
			C.append(0)

		for j in range(0, len(A)):
			C[A[j]] += 1

		for i in range(1, k+1):
			C[i] = C[i] + C[i-1]
			
		for j in range(len(A)-1, -1, -1):
			B[C[A[j]]-1] = A[j]
			C[A[j]] -= 1

def rangeCountPre(A, C, k):
	if len(A) > 1:
		for i in range(0, k+1):
			C.append(0)

		for j in range(0, len(A)):
			C[A[j]] += 1

		for i in range(1, k+1):
			C[i] = C[i] + C[i-1]

def rangeCount(C, a, b):
	if a < 1:
		return C[b]
	else:
		return C[b] - C[a-1]

if __name__ == '__main__':
	# Sets up random
	# random.seed(time.time())

	# Arrays to sort
	k = 100
	A1 = [random.randint(0, k) for i in range(k)]
	A2 = [i for i in range(k)]
	A3 = [i for i in range(k - 1, -1, -1)]
	A4 = [100] * 100
	# A5 = [random.randint(ranges[0], ranges[1]) * -1 for i in range(100)]

	# Sorts
	# A1 = [4, 7, 9, 1, 0, 15]
	B = [0] * len(A1)
	print(A1, end='\n\n')
	countingSort(A1, B, max(A1))
	print(B)

	A5 = [2, 4, 2, 1, 1, 5, 0, 10, 7, 8]
	C = []
	rangeCountPre(A5, C, max(A5))
	print(C)
	c1 = rangeCount(C, 0, 5)
	c2 = rangeCount(C, 6, 10)
	print(c1, c2)