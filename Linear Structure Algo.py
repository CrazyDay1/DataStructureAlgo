import time
unsort = [10,16,8,12,15,6,3,19,5]
start = time.time()

# whole thing functions like a binary tree(breakdown into smaller nodes), then combine the tree back while sorting 
def mergesort(arr):
  if len(arr) <= 1: # check if element in list is less than equal onem if yes return list
    return arr
    
  mid = len(arr) // 2  # divide len of list into 2, split the list 

  left = arr[:mid] # break list into 2 part 
  right = arr[mid:]

  mergesort(left) # recursively call the function until only 1 part 
  mergesort(right)

  i = j = k = 0  # declare pointer 

  while i < len(left) and j < len(right):  # loop through left and right list, pick the smaller number throw into list 
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1

    k += 1

  while i < len(left): # check for any left over number in list
    arr[k] = left[i]
    k += 1
    i += 1

  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1

  return arr

def partition(start, end):
  i = start + 1 # put as variable for ease of use 
  j = end 
  pivot = unsort[start]

  while j >= i: # loop while j <= i, so it doesnt mess up later 
    if unsort[i] <= pivot:
      i += 1

    if unsort[j] >= pivot:
      j -= 1

    if j >= i: # simple swap
      unsort[i], unsort[j] = unsort[j], unsort[i]

  unsort[start], unsort[j] = unsort[j], unsort[start] # swap j  (last element of smallest) with pivot 

  return j # to act as midpoint 

def quicksort(start, end):
  if end > start: # in charge of telling the loop to break until has at least 1 element 
    pivot = partition(start, end) # get middle point 
    quicksort(start, pivot - 1) # deal with left side 
    quicksort(pivot + 1, end) # deal with right side 

def bubblesort():
  for i in range(len(unsort) - 1):
    for j in range(len(unsort) - i - 1): # assume i element sorted alr 
      if unsort[j] > unsort[j + 1]: # if next smaller than current, swap 
        unsort[j], unsort[j + 1] = unsort[j + 1], unsort[j]


def insertsort():
  for i in range(1, len(unsort)): # start at first element, easier 
    key = unsort[i] # key to compare 
    j = i - 1 

    while j >= 0 and unsort[j] > key: # only activte the loop if the imediate element in front is bigger than key
      unsort[j + 1] = unsort[j] # shiftup/ makeway to insert key later 
      j -= 1 # at last interation this will make the element to be one less 

    unsort[j + 1] = key # thus add one and put key inside 

quicksort(0, len(unsort) - 1)
end = time.time()
print(f"Time taken: {end - start}")
print(unsort)