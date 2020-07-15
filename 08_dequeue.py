class Deque(object):
	"""双端队列(double-end queue,deque)"""
	def __init__(self):
		self.__list = []

	def add_front(self, item):
		"""头进"""
		self.__list.insert(0, item)

	def add_rear(self, item):
		"""尾进"""
		self.__list.append(item)

	def remove_front(self):
		"""头删"""
		return self.__list.pop(0)

	def remove_rear(self):
		"""尾删"""
		return self.__list.pop()

	def is_empty(self):
		"""判断一个队列是否为空"""
		return self.__list == []

	def size(self):
		"""返回队列的大小"""
		return len(self.__list)

	def travel(self):
		"""遍历队列"""
		for i in self.__list:
			print(i)


if __name__ == "__main__":
	q = Deque()

	q.add_front(1)
	q.add_front(2)

	q.add_rear(3)

	q.travel()

