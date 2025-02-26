def insertion_sort(arr):
  for k in range(1, len(arr)):
    cur = arr[k]
    j = k
    while j > 0 and arr[j-1] > cur:
      arr[j] = arr[j-1]
      j = j - 1
    arr[j] = cur

a = [8,2,-4,9,8]
insertion_sort(a)
print(a)