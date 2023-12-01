def stooge_sort(arr, l, h):
	if l >= h:
		return
	if arr[l]>arr[h]:
		arr[l],arr[h]=arr[h],arr[l]

		# PLACE HERE TO SHOW SWAPS
		yield (l,h)

	if h-l+1>2:
		temp=int((h-l+1)/3)
		yield from stooge_sort(arr,l,h-temp)
		yield from stooge_sort(arr,l+temp,h)
		yield from stooge_sort(arr,l,h-temp)
	# yield (l,h)

def cocktail_shaker_sort(array,len):
	swap = True
	start = 0
	end = len-1
	while(swap):
		swap = False
		for a in range(start,end):
			if array[a] > array[a+1]:
				array[a], array[a + 1] = array[a + 1], array[a]
				swap = True
				yield (a,a)
			if not swap:
				end = end-1;
		for b in range(end-1,start-1,-1):
			if array[b]>array[b+1]:
				array[b],array [b+1] = array[b+1],array[b]
				swap = True
				yield(b,b)
		start+=1

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
		yield(n,n)