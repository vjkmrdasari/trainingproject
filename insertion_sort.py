def insertion_sort(arr):
  for i in range(1,len(arr)):
    key = arr[i]
    j=i-1

    while j>=0 and arr[j]>key:
      arr[j+1],arr[j] = arr[j],arr[j+1]
      j-=1

  return arr
data = [8, 4, 6, 2]
print("Sorted array:", insertion_sort(data))