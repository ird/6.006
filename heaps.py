def left(heap, node):
    """
    Returns the index of the root of the left sub-tree of a heap implemented as an array
    A[2n+1] = root of left sub tree of A[n]
    """
    l = 2*node+1
    if l > len(heap):
        raise IndexError
    if heap[l] == None:
        raise IndexError
    return l

def right(heap, node):
    """
    Returns the index of the root of the left sub-tree of a heap implemented as an array
    A[2n+1] = root of left sub tree of A[n]
    """
    r = 2*node+2
    if r > len(heap):
        raise IndexError
    if heap[r] == None:
        raise IndexError
    return r

def max_heapify(heap, root):
    """
    Pre-condition: the trees anchored at left(heap,0) and right(heap,0) are already max-heaps
    Returns heap as a max-heap in O(lg n) by correcting the violation of the max-heap-property
    at the heap's root.
    """
    largest = select_new_root(heap, root)
    if largest == "root":
        return heap
    if largest == "left":
        l = left(heap, root)
        t = heap[l]
        heap[l] = heap[root]
        heap[root] = t
        return max_heapify(heap, l)
    if largest == "right":
        r = right(heap, root)
        t = heap[r]
        heap[r] = heap[root]
        heap[root] = t
        return max_heapify(heap, r)

def select_new_root(heap, root):
    """
    select_new_root() is a utility function that returns "root", "left" or "right" depending on
    whether the existing root, left sub-tree root or right sub-tree root is largest, respectively.
    This prevents calling left(heap, root) [etc] if one does not exist as this function handles
    IndexErrors as they occur.
    """
    try:
        left = left(heap, root)
        try:
            right = right(heap, root)
            # there is a right and a left sub tree
            if heap[left] >= heap[right]:
                return "root" if heap[root] >= heap[left] else "left"
            else:
                return "root" if heap[root] >= heap[right] else "right"
        except:
            # there is a left sub-tree but no right sub-tree
            return "root" if heap[root] >= heap[left] else "left"
    except:
        # there is no left sub tree
        try:
            return "root" if heap[root] >= heap[right] else "right"
        except:
            return "root" # there are no children


def build_heap(array):
    """
    Build a max heap from an unsorted array in O(n)
    """
    pass

def main():
    heap = [16,14,10,7,6,1,2]
    print(heap[left(heap, 1)])

if __name__ == "__main__":
    main()
