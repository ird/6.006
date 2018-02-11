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
        print("nothing left to change")
        return heap
    if largest == "left":
        l = left(heap, root)
        print("at", root, "new root should be (left)", l)
        t = heap[l]
        heap[l] = heap[root]
        heap[root] = t
        return max_heapify(heap, l)
    if largest == "right":
        r = right(heap, root)
        print("at", root, "new root should be (right)", r)
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
        l = left(heap, root)
        try:
            r = right(heap, root)
            if heap[l] >= heap[r]:
                # print("left is bigger than right, so testing heap[l]")
                return "root" if heap[root] >= heap[l] else "left"
            else:
                # print("right is bigger than left, so testing heap[r]")
                return "root" if heap[root] >= heap[r] else "right"
        except:
            # print("there is no right sub-tree")
            return "root" if heap[root] >= heap[l] else "left"
    except:
        try:
            # print("there is no left sub-tree")
            return "root" if heap[root] >= heap[r] else "right"
        except:
            # print("there are no leaves")
            return "root" # there are no children


def build_heap(array):
    """
    Build a max heap from an unsorted array in O(n)
    """
    pass

def main():
    heap = [4,15,11,7,6,1,2]
    print(select_new_root(heap, 0))
    print(max_heapify(heap, 0))

def test():
    heap = [4, 5, 0]
    assert(select_new_root(heap, 0) == "left")
    assert(max_heapify(heap, 0) == [5, 4, 0])
    heap = [1, 1, 3]
    assert(select_new_root(heap, 0) == "right")
    assert(max_heapify(heap, 0) == [3, 1, 1])
    heap = [10, 4, 5]
    assert(select_new_root(heap, 1) == "root")
    heap = [10, 11, 8, 16, 17]
    assert(max_heapify(heap, 0) == [11, 17, 8, 16, 10])


if __name__ == "__main__":
    main()
