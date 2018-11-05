from quickSort import *
import random, time

def randSelect(A, p, r, i):
	if p == r:
		return A[p]

	q = randPart(A, p, r)

	k = q - p + 1

	if i == k:
		return A[q]

	if i < k:
		return randSelect(A, p, q-1, i)

	else:
		return randSelect(A, q+1, r, i-k)

if __name__ == '__main__':
	# Arrays to sort
	s = 10
	A1 = [random.randint(0, s) for i in range(s)]
	print(A1)

	ith = randSelect(A1, 0, len(A1)-1, len(A1))

	print(ith)