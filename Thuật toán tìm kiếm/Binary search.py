def binary_search(a, b):
    trai, phai = 0, len(a) - 1

    while trai <= phai:
        mid = (trai + phai) // 2
        if a[mid] == b:
            return mid
        elif a[mid] < b:
            trai = mid + 1
        else:
            phai = mid - 1

    return -1
