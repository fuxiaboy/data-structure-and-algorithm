def bubble_sort(alist):
	"""冒泡排序"""
	n = len(alist)
	# 外层循环管趟数（一共比较多少趟）
	for j in range(0, n-1):
		count = 0
		# 内层循环管次数（每趟比较多少次）
		for i in range(0, n-1-j):
			# 降序
			# if alist[i] < alist[i+1]:
			# 升序
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				count += 1
		if count == 0:
			return

alist = [0, 6, 3, 1, 2, 8]
print(alist)
bubble_sort(alist)
print(alist)

