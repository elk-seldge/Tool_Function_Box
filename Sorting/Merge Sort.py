def Merge(arr1, arr2):
	rtn = []
	lngth = len(arr1) + len(arr2)
	while lngth > 0:
		if not len(arr1):
			rtn += arr2
			break
		if not len(arr2):
			rtn += arr1
			break
		if arr1[0] < arr2[0]:
			rtn.append(arr1.pop(0))
			lngth -= 1
		else:
			rtn.append(arr2.pop(0))
			lngth -= 1
		return rtn


def MergeSort(arr, start, end):
	mid = len(arr)//2
	MergeSort(arr, start, mid)
	MergeSort(arr, mid, end)
	Merge(arr
	

	
