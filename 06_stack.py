class Stack(object):
	"""栈"""
	def __init__(self):
		self.__list = []

	def push(self, item):
		"""入栈"""
		#         时间复杂度
		# append	O(1)
		# insert	O(n)
		# self.__list.insert(0, item)
		self.__list.append(item)

	def pop(self):
		"""出栈"""
		#      时间复杂度
		# pop     O(1)
		# pop(0)  O(n)
		return self.__list.pop()

	def peek(self):
		"""返回栈顶元素"""
		if self.__list:
			return self.__list[-1]
		else:
			return None

	def is_empty(self):
		"""判断栈是否为空"""
		# return not self.__list
		return self.__list == []

	def size(self):
		"""返回栈的元素个数"""
		return len(self.__list)


if __name__ == "__main__":
	s = Stack()

	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)

	# print(s.pop())
	# print(s.pop())
	# print(s.pop())
	# print(s.pop())

	print(s.is_empty())
	print(s.size())

