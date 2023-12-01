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


def counting_sort(arr, exp, l, h):
    n = h - l + 1
    output = [0] * n
    count = [0] * 10

    for i in range(l, h + 1):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = h
    while i >= l:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(l, h + 1):
        arr[i] = output[i - l]

        # PLACE HERE TO SHOW SWAPS
        yield (i, i)

def radix_sort(arr, l, h):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        yield from counting_sort(arr, exp, l, h)
        exp *= 10



# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
n = len(arr)

# Visualize radix sort
for swap in radix_sort(arr, 0, n - 1):
	print("Swap:", swap)

print("Sorted array:", arr)

