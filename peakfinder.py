
def list_peak_finder(L, start=0, end=None):
    """
    Definition: A peak exists at n L[n] where L[n] >= L[n-1], L[n+1].
    If L[n] only has one neighbour, then it is sufficient that it is greater
    than that neighbour only.
    Returns the peak.
    Complexity:
    T(n) = time take for an operation on list of size n. Then:
    T(n) = T(n/2) + c
         = T(n/4) + c + c
         ...lg n times
         = T(1) + lg(n)*c
    so, T(n) = Th(lg n)
    """
    if end == None:
        end = len(L)
    size = end - start
    n = start + (size >> 1)
    if size > 2:
        if L[n-1] >= L[n]:
            return list_peak_finder(L, start, n)
        if L[n+1] >= L[n]:
            return list_peak_finder(L, n+1, end)
    if size == 1:
        pass
    if size == 2:
        if L[n-1] >= L[n]:
            return L[n-1]
    return L[n]

def main():
    print(list_peak_finder([1,2,3,4,6,7]))

if __name__ == "__main__":
    main()
