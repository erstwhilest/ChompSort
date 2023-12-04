import time


def compare_and_swap(arr, i, j, direction):
	if (arr[i] > arr[j] and direction) or (arr[i] < arr[j] and not direction):
		arr[i], arr[j] = arr[j], arr[i]


# merges the chunks together called by sort
def bitonic_merge(arr, l, count, direction):
	if count > 1:
		k = count // 2
		for i in range(l, l + k):
			compare_and_swap(arr, i, i + k, direction)
		bitonic_merge(arr, l, k, direction)
		bitonic_merge(arr, l + k, k, direction)


# Sorts a part of the list in ascending order, then another part in descending order
# then merges it back together
def bitonic_sort(arr, l, count, direction):
	if count > 1:
		k = count // 2
		bitonic_sort(arr, l, k, True)
		bitonic_sort(arr, l + k, k, False)
		bitonic_merge(arr, l, count, direction)

def sort_bitonic(arr):
	n = len(arr)
	direction = True  # True represents sorting in ascending order, False for descending
	bitonic_sort(arr, 0, n, direction)

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

def counting_sort(arr, exp):
	n = len(arr)
	output = [0] * n
	count = [0] * 10

	for i in range(n):
		index = arr[i] // exp
		count[index % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	while i >= 0:
		index = arr[i] // exp
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	for i in range(n):
		arr[i] = output[i]

def cycle_sort(array):
	writes = 0
	for cycle_start in range(0, len(array) - 1):
		item = array[cycle_start]
		pos = cycle_start
		for i in range(cycle_start + 1, len(array)):
			if array[i] < item:
				pos += 1
		if pos == cycle_start:
			continue
		while item == array[pos]:
			pos += 1
		array[pos], item = item, array[pos]
		writes += 1
		while pos != cycle_start:
			pos = cycle_start
			for i in range(cycle_start + 1, len(array)):
				if array[i] < item:
					pos += 1
			while item == array[pos]:
				pos += 1
			array[pos], item = item, array[pos]
			writes += 1

def radix_sort(arr):
	max_num = max(arr)
	exp = 1

	while max_num // exp > 0:
		counting_sort(arr, exp)
		exp *= 10

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
    elif(sortfunction == "Radix Sort"):
        start = time.time()
        radix_sort(data)
        end = time.time()
        return(end-start)*1000
    elif(sortfunction == "Cycle Sort"):
        start = time.time()
        cycle_sort(data)
        end = time.time()
        return (end-start)*1000
    elif(sortfunction == "Bitonic Sort"):
        start = time.time()
        sort_bitonic(data)
        end = time.time()
        return (end-start)*1000
