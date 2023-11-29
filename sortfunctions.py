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