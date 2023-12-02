import time
def stooge_sort(arr, l, h):
	if l >= h:
		return
	if arr[l]>arr[h]:
		arr[l],arr[h]=arr[h],arr[l]

	if h-l+1>2:
		temp=int((h-l+1)/3)

def stooge_sort(arr, l, h):
	if l >= h:
		return
	if arr[l]>arr[h]:
		arr[l],arr[h]=arr[h],arr[l]
	if h-l+1>2:
		temp=int((h-l+1)/3)
	# yield (l,h)

def cocktail_shaker_sort(array):
	for i in range(len(array)-1,0,-1):
		is_swapped = False
		for j in range(i,0,-1):
			if array[j] < array [j-1]:
				array[j],array[j-1]=array[j-1],array[j]
				is_swapped = True
		for j in range(i):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				is_swapped = True
		if not is_swapped:
			break

#pancake + helper functions
def max_index(arr, k):
	index = 0
	for i in range(k):
		if arr[i] > arr[index]:
			index = i
	#returns max index
	return index
def flip(arr, k):
	left = 0
	while left < k:
		arr[left], arr[k] = arr[k], arr[left]
		k -= 1
		left += 1
def pancake_sort(arr):
	n = len(arr)
	while n > 1:
		maxIndex = max_index(arr, n)
		if maxIndex != n:
			#flip function reverses list
			flip(arr, maxIndex)
			flip(arr, n - 1)
		n -= 1

#pancake + helper functions
def max_index(arr, k):
	index = 0
	for i in range(k):
		if arr[i] > arr[index]:
			index = i
	#returns max index
	return index
def flip(arr, k):
	left = 0
	while left < k:
		arr[left], arr[k] = arr[k], arr[left]
		k -= 1
		left += 1
def pancake_sort(arr):
	n = len(arr)
	while n > 1:
		maxIndex = max_index(arr, n)
		if maxIndex != n:
			#flip function reverses list
			flip(arr, maxIndex)
			flip(arr, n - 1)
		n -= 1


def test(sortfunction, data):
    if(sortfunction == "Pancake Sort"):
        start = time.time()
        pancake_sort(data)
        end = time.time()
        return (end-start)*1000
    elif(sortfunction == "Cocktail Shaker Sort"):
        start = time.time()
        cocktail_shaker_sort(data)
        end = time.time()
        return (end-start)*1000
    elif(sortfunction == "Stooge Sort"):

        start = time.time()

        stooge_sort(data,0,len(data)-1)
        end = time.time()
        return (end-start)*1000