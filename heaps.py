from timeit import default_timer as timer
from random import randint
import cProfile

def max_heapify(heap, root, size):
    """
    Pre-condition: the trees anchored at left(heap,0) and right(heap,0) are already max-heaps
    Returns heap as a max-heap in O(lg n) by correcting the violation of the max-heap-property
    at the heap's root.
    """
    l = 2*root+1
    r = 2*root+2
    if size <= l:
        # no children at root
        return
    elif size <= r:
        # only a left child
        if heap[l] > heap[root]:
            heap[l], heap[root] = heap[root], heap[l]
            return max_heapify(heap, l, size)
        else:
            return
    else:
        if heap[l] > heap[r]:
            if heap[l] > heap[root]:
                heap[l], heap[root] = heap[root], heap[l]
                return max_heapify(heap, l, size)
            else:
                return
        else:
            if heap[r] > heap[root]:
                heap[r], heap[root] = heap[root], heap[r]
                return max_heapify(heap, r, size)
            else:
                return

def build_heap(array):
    """
    Build a max heap from an unsorted array in O(n)
    """
    heap = array[:]
    size = len(heap)
    n = size >> 1
    for i in range(n, -1, -1):
        max_heapify(heap, i, size)
    return heap

def extract_max(heap):
    """
    Extract the max item and leave the max-heap intact
    """
    max = heap[0]
    heap[0] = heap[len(heap)-1]
    heap.pop()
    max_heapify(heap, 0, len(heap))
    return max

def heapsort(array):
    heap = build_heap(array)
    for i in range(0, len(heap)):
        array[i] = extract_max(heap)

def main():
    long_list = []
    for i in range(10000):
        long_list.append(randint(0, 999))
    start = timer()
    cProfile.runctx("heapsort(long_list)", globals(), locals())
    test1 = timer()-start
    print("Time taken, heapsort: ", test1)

def test():
    # run "py.test heaps.py"
    heap = [4, 5, 0]
    max_heapify(heap, 0, len(heap))
    assert(heap == [5, 4, 0])
    heap = [1, 1, 3]
    max_heapify(heap, 0, len(heap))
    assert(heap == [3, 1, 1])
    heap = [10, 11, 8, 16, 17]
    max_heapify(heap, 0, len(heap))
    assert(heap == [11, 17, 8, 16, 10])
    assert(build_heap([4,15,11,7,6,18,2]) == [18,15,11,7,6,4,2])
    array = [1,2,3,4,5,6,7,8,9,10,11]
    heapsort(array)
    assert(array == [11,10,9,8,7,6,5,4,3,2,1])


if __name__ == "__main__":
    main()
