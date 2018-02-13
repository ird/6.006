from timeit import default_timer as timer
from random import randint
def merge(a, b):
    """ merge two already sorted lists """
    s = []
    index_a = 0;
    index_b = 0;

    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            s.append(a[index_a])
            index_a += 1
        else:
            s.append(b[index_b])
            index_b += 1
    if index_a == len(a):
        s.extend(b[index_b:])
    else:
        s.extend(a[index_a:])
    return s

def mergesort(L, i=0, j=None):
    """ mergesort that does not alter the original list """
    j = len(L) if j == None else j
    size = j - i
    if size == 1:
        return [L[i]]
    else:
        m = size >> 1
        return merge(mergesort(L, i, i+m), mergesort(L, i+m, j))

def mergesort_slice(L):
    """ mergesort that slices L each time """
    if len(L) == 1:
        return L
    else:
        m = len(L) >> 1
        return merge(mergesort_slice(L[0:m]), mergesort_slice(L[m:]))

def main():
    print(merge([1,5,7,9], [2,4,6]))
    print(mergesort([5,4,6,7,3,1,2,9,8]))
    print(mergesort_slice([5,4,6,7,3,1,2,9,8]))
    long_list = []
    for i in range(10000):
        long_list.append(randint(0, 999))
    start = timer()
    mergesort(long_list)
    test1 = timer()-start
    print("Time taken, mergesort without slices: ", test1)
    start = timer()
    mergesort_slice(long_list)
    test2 = timer()-start
    print("Time taken, mergesort with slices: ", test2)
    print("Ratio: ", test2/test1)
    start = timer()
    long_list.sort()
    print("Time taken, .sort(): ", timer()-start)
    
if __name__ == "__main__":
    main()
