def linear_search(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    return -1  
