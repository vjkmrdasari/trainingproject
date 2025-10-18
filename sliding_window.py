def max_sum_sliding_window(arr, k):
  window_sum = sum(arr[:k])
  max_sum = window_sum

  for i in range (k, len(arr)):
    window_sum += arr[i]-arr[i-k]
    max_sum = max(window_sum,max_sum)

  return max_sum


# Example:
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_sliding_window(arr, k))  # Output: 39