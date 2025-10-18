def first_occurence(a,t):
    start = 0
    end = len(a)-1
    result = -1
    while start < end:
        mid = (start+end)//2
        if a[mid] == t:
            result = mid
            start = mid+1
        elif a[mid] < t:
            end = mid-1
        else:
            start = mid+1
    return result

def last_occurence(a,t):
    start = 0
    end = len(a)-1
    result = -1
    while start <= end:
        mid = (start+end)//2
        if a[mid] == t:
            result = mid
            start = mid+1
        elif a[mid] < t:
            start = mid+1
        else:
            end = mid-1
    return result
arr = [1, 1, 2, 2, 3, 4]
print(first_occurence(arr, 2))  # 2
print(last_occurence(arr, 2))   # 3