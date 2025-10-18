def find_peak_binary(a):
    start = 0
    end = len(a)-1
    while start<end:
        mid = (start+end)//2
        if a[mid]<a[mid+1]:
            start = mid+1
        else:
            end = mid
    return start

arr = [1, 3, 20, 4, 1, 0]
print(find_peak_binary(arr))