def select_sort(alist):
	"""选择排序"""
	n = len(alist)
	for j in range(0, n-1):  # j：0 ~ n-2
		min_index = j
		for i in range(j+1, n):
			if alist[min_index] > alist[i]:
				min_index = i
		alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
	alist = [5, 4, 3, 2, 1, 0]
	print(alist)
	select_sort(alist)
	print(alist)