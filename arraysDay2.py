# this function is a mutator

def set_value_at(arr,index,val):
  if index < 0 or index >= len(arr):
    return
  
  arr[index] = val

  # this doesn't work
  #b = [None] * len(arr)
  #for i in range(len(arr)):
  #  b[i] = arr[i]
  #b[index] = val
  #arr = b

a = [4,15,-5,6]
set_value_at(a,1,-2)
print(a)