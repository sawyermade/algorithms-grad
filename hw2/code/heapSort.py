# Global
swapCount = 0

def heapSort(A):
    global swapCount
    # Builds max heap
    buildMaxHeap(A)

    # Sets heapsize n, swaps and heapifies all in reverse order
    n = len(A)
    for i in range(len(A)-1, 0, -1):
        swap(A, 0, i)
        swapCount += 1
        n -= 1
        print(A)
        maxHeapify(A, 0, n)

def buildMaxHeap(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        maxHeapify(A, i, n)
    print(A)

def maxHeapify(A, i, n):
    global swapCount
    # Sets left, right, largest
    l = 2*i + 1
    r = l + 1
    largest = i

    # Finds largest
    if l < n and A[largest] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    # If i isnt largest
    if largest != i:
        swap(A, i, largest)
        swapCount += 1
        print(A)
        maxHeapify(A, largest, n)

def swap(A, i, largest):
    t = A[i]
    A[i] = A[largest]
    A[largest] = t

def main():
    global swapCount
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    B = [5, 13, 2, 25, 7, 17, 20, 8, 4]

    print(A)
    heapSort(A)
    print('swapCount = {}\n'.format(swapCount))
    swapCount = 0

    print(B)
    heapSort(B)
    print('swapCount = {}\n'.format(swapCount))
    swapCount = 0

if __name__ == '__main__':
    main()