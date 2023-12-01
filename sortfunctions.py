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
	# PLACE HERE TO SHOW ALL COMPARISONS
	# yield (l,h)

def cycle_sort(array):
	writes = 0

	for cycle_start in range(0, len(array) - 1):
		item = array[cycle_start]

		pos = cycle_start
		for i in range(cycle_start + 1, len(array)):
			if array[i] < item:
				yield (i, item-1)
				# yield
				pos += 1

		if pos == cycle_start:
			continue

		while item == array[pos]:
			pos += 1
		
		array[pos], item = item, array[pos]
		writes += 1

		yield (cycle_start, pos)
		# yield

		while pos != cycle_start:

			pos = cycle_start
			for i in range(cycle_start + 1, len(array)):
				if array[i] < item:
					yield (i, item-1)
					# yield
					pos += 1

			while item == array[pos]:
				pos += 1
			array[pos], item = item, array[pos]
			writes += 1

			yield (item-1, pos)
			# yield