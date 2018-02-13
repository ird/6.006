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
    if size <= l:
        # no children at root
        return
    r = l+1
    if size <= r:
        # only a left child
        if heap[l] > heap[root]:
            heap[l], heap[root] = heap[root], heap[l]
            return max_heapify(heap, l, size)
    else:
        if heap[l] > heap[r]:
            if heap[l] > heap[root]:
                heap[l], heap[root] = heap[root], heap[l]
                return max_heapify(heap, l, size)
        else:
            if heap[r] > heap[root]:
                heap[r], heap[root] = heap[root], heap[r]
                return max_heapify(heap, r, size)

def max_heapify_iter(heap, root=0):
    """
    Non-recursive version of max_heapify().
    Pre-condition: the trees anchored at left(heap,0) and right(heap,0) are already max-heaps
    Returns heap as a max-heap in O(lg n) by correcting the violation of the max-heap-property
    at the heap's root.
    """
    size = len(heap)
    while True:
        l = 2*root+1
        if size <= l:
            # no children at root
            break
        r = l+1
        if size <= r:
            # only a left child
            if heap[l] > heap[root]:
                heap[l], heap[root] = heap[root], heap[l]
                root = l
                continue
        else:
            if heap[l] > heap[r]:
                if heap[l] > heap[root]:
                    heap[l], heap[root] = heap[root], heap[l]
                    root = l
                    continue
            else:
                if heap[r] > heap[root]:
                    heap[r], heap[root] = heap[root], heap[r]
                    root = r
                    continue
        break

def build_heap(array):
    """
    Build a max heap from an unsorted array in O(n)
    """
    heap = array[:]
    size = len(heap)
    n = size >> 1
    for i in range(n, -1, -1):
        max_heapify_iter(heap, i)
    return heap

def extract_max(heap):
    """
    Extract the max item and leave the max-heap intact
    """
    max = heap[0]
    heap[0] = heap[len(heap)-1]
    heap.pop()
    max_heapify_iter(heap)
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
    max_heapify_iter(heap)
    assert(heap == [5, 4, 0])
    heap = [1, 1, 3]
    max_heapify_iter(heap)
    assert(heap == [3, 1, 1])
    heap = [10, 12, 8, 6, 11]
    max_heapify_iter(heap)
    assert(heap == [12, 11, 8, 6, 10])
    assert(build_heap([4,15,11,7,6,18,2]) == [18,15,11,7,6,4,2])
    array = [1,2,3,4,5,6,7,8,9,10,11]
    heapsort(array)
    assert(array == [11,10,9,8,7,6,5,4,3,2,1])


if __name__ == "__main__":
    main()
