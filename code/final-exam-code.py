def lcs(A):

	C = [0]*len(A)
	D = [0]*len(A)

	max1 = 0
	C[0] = A[0]
	for i in range(1, len(A)):
		C[i] = C[i-1] + A[i]

		if C[max1] < C[i]:
			max1 = i

	D[-1] = A[-1]
	max2 = len(A) - 1
	for i in range(len(A)-2, -1, -1):
		D[i] = D[i+1] + A[i]

		if D[max2] < D[i]:
			max2 = i

	print(C)
	print(D)

	return A[max2:max1+1]

def ab(A):
	acount = 0
	bcount = 0
	for val in A:
		if val == 'a':
			acount += 1
		else:
			bcount += 1

	for i in range(len(A)):
		if i <= acount:
			A[i] = 'a'
		else:
			A[i] = 'b'

if __name__ == '__main__':

	A = [-3, 7, 4, -4, 5, -2, -9]

	B = lcs(A)

	print(B)
	print(sum(B))

	A = ['a', 'b', 'b', 'b', 'a', 'a', 'b', 'b', 'a']
	ab(A)
	print(A)