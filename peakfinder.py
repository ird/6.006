def list_peak_finder(L, n=0):
    """
    A peak exists at n L[n] where L[n] >= L[n-1], L[n+1].
    If L[n] only has one neighbour, then it is sufficient that it is greater
    than that neighbour only.

    Returns the index of the peak. 
    
    """
    # exit criteria
    
    # pick the middle of the list
    
    if n > 0 and L[n-1] >= L[n]:
        return list_peak_finder(L, n-1)
    if n < len(L)-1 and L[n+1] >= L[n]:
        return list_peak_finder(L, n+1)
    return n

def main():
    pass

if __name__ == "__main__":
    main()   
