def list_peak_finder(L, start=0, end=None):
    """
    A peak exists at n L[n] where L[n] >= L[n-1], L[n+1].
    If L[n] only has one neighbour, then it is sufficient that it is greater
    than that neighbour only.

    Returns the peak.
    """
    if end == None:
        end = len(L) - 1
    n = start + (end - start >> 1)
    if n > start and L[n-1] >= L[n]:
        return list_peak_finder(L, start, n-1)
    if n < end and L[n+1] >= L[n]:
        return list_peak_finder(L, n+1, end)
    return L[n]

def main():
    print(list_peak_finder([5,6,7,8,82,1]))

if __name__ == "__main__":
    main()   
