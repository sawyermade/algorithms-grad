class PriorityQueue:
    # Init, A is original array, B is heapSort var, C
    def __init__(self, A):
        # Original
        self.A = [f for f in A]
        
        # Max Heap
        self.maxHeap = [f for f in A]
        self.buildMaxHeap(self.maxHeap)
        
        # Min Heap
        self.minHeap = [f for f in A]
        self.buildMinHeap(self.minHeap)

        # Max heap sorted
        self.maxHeapSorted = None
        self.maxHeapSort()

        # Min heap sorted
        self.minHeapSorted = None
        self.minHeapSort()

    # Returns min
    @property
    def min(self):
        return self.minHeap[0]
    # Returns max
    @property
    def max(self):
        return self.maxHeap[0]

    # Inserts and bubbles up for min and max
    def insert(self, val):
        # Increase heapsize and append value
        self.A.append(val)
        self.maxHeap.append(val)
        self.minHeap.append(val)

        # Gets size and info to find parent
        A = self.maxHeap
        n = len(A)
        i = n-1

        # Gets parent and bubbles it up
        p = self.parent(i)
        while i > 0 and A[p] < A[i]:
            self.swap(A, i, p)
            i = p
            p = self.parent(i)

        # Min heap insert
        A = self.minHeap
        n = len(A)
        i = n-1
        p = self.parent(i)
        while i > 0 and A[p] > A[i]:
            self.swap(A, i, p)
            i = p
            p = self.parent(i)

    # Finds parent in array
    def parent(self, i):
        # Even or odd
        if i % 2 == 0:
            lr = 2
        else:
            lr = 1

        # Returns parent index
        return (i-lr)//2


    # Max heap sort
    def maxHeapSort(self):
        A = self.maxHeapSorted = [f for f in self.A]
        # Builds max heap
        self.buildMaxHeap(A)

        # Sets heapsize n, swaps and heapifies all in reverse order
        n = len(A)
        for i in range(len(A)-1, 0, -1):
            self.swap(A, 0, i)
            n -= 1
            self.maxHeapify(A, 0, n)

    # Min heap sort
    def minHeapSort(self):
        A = self.minHeapSorted = [f for f in self.A]
        # Builds max heap
        self.buildMinHeap(A)

        # Sets heapsize n, swaps and heapifies all in reverse order
        n = len(A)
        for i in range(len(A)-1, 0, -1):
            self.swap(A, 0, i)
            n -= 1
            self.minHeapify(A, 0, n)

    # Builds max heap
    def buildMaxHeap(self, A):
        n = len(A)
        for i in range(n//2, -1, -1):
            self.maxHeapify(A, i, n)

    # Builds min heap
    def buildMinHeap(self, A):
        n = len(A)
        for i in range(n//2, -1, -1):
            self.minHeapify(A, i, n)

    # Max Heapify
    def maxHeapify(self, A, i, n):
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
            self.swap(A, i, largest)
            self.maxHeapify(A, largest, n)

    # Min Heapify
    def minHeapify(self, A, i, n):
        # Sets left, right, smallest
        l = 2*i + 1
        r = l + 1
        smallest = i

        # Finds smallest
        if l < n and A[l] < A[smallest]:
            smallest = l

        if r < n and A[r] < A[smallest]:
            smallest = r

        # If i isnt smallest
        if smallest != i:
            self.swap(A, i, smallest)
            self.minHeapify(A, smallest, n)

    # Swaps indices a and b in A
    def swap(self, A, a, b):
        temp = A[a]
        A[a] = A[b]
        A[b] = temp

    # For printing
    def __str__(self):
        a = ', '.join([str(f) for f in self.A]) + ' :Original' + '\n'
        maxHeap = ', '.join([str(f) for f in self.maxHeap]) + ' :Max Heap' + '\n'
        minHeap = ', '.join([str(f) for f in self.minHeap]) + ' :Min Heap' + '\n'
        maxHeapSorted = ', '.join([str(f) for f in self.maxHeapSorted]) + ' :Max Sort' + '\n'
        minHeapSorted = ', '.join([str(f) for f in self.minHeapSorted]) + ' :Min Sort' + '\n'
        return a + minHeap + minHeapSorted + maxHeap + maxHeapSorted

def main():
    # Arrays to heapify/sort/priority queue
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    B = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    
    # Builds heaps
    pqa = PriorityQueue(A)
    pqb = PriorityQueue(B)

    # Prints heaps
    print(pqa)
    print(pqb)

    # Prints min/max
    print('min/max = {}/{}'.format(pqa.min, pqa.max))
    print('min/max = {}/{}'.format(pqb.min, pqb.max))
    print()

    # Inserts new values
    pqa.insert(69)
    pqa.maxHeapSort()
    pqa.minHeapSort()
    pqb.insert(69)
    pqb.maxHeapSort()
    pqb.minHeapSort()

    # Prints again
    print(pqa)
    print(pqb)

    # Prints min/max
    print('min/max = {}/{}'.format(pqa.min, pqa.max))
    print('min/max = {}/{}'.format(pqb.min, pqb.max))
    print()

if __name__ == '__main__':
    main()