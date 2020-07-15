class Node(object):
	"""单向链表的结点"""

	def __init__(self, elem):
		self.elem = elem
		self.next = None


class SingleLinkList(object):
	"""单向链表"""

	def __init__(self, node=None):
		self.__head = node

	def is_empty(self):
		"""判断链表是否为空"""
		return self.__head is None

	def length(self):
		"""链表长度"""
		# cur：游标，用来移动遍历结点
		cur = self.__head
		# count：记录数量
		count = 0
		while cur is not None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur is not None:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")

	def add(self, item):
		"""链表头部添加结点，头插法"""
		node = Node(item)
		node.next = self.__head
		self.__head = node

	def append(self, item):
		"""链表尾部添加结点，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next is not None:
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		"""指定位置添加结点
		:param pos 从0开始
		"""
		node = Node(item)
		if pos <= 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			pre = self.__head
			# for i in range(pos - 1):
			#   pre = pre.next
			count = 0
			while count < (pos - 1):
				count += 1
				pre = pre.next
			# 当退出循环后，pre指向 pos - 1 的位置
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		"""删除结点"""

		cur = self.__head
		pre = None
		while cur is not None:
			if cur.elem == item:
				# 先判断此结点是否是头结点				
				if cur == self.__head:  # 头结点
					self.__head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

		# if self.__head == None:
		# 	print("该链表为空！")
		# else:
		# 	cur = self.__head
		# 	pre = self.__head
		# 	count = 0
		# 	i = 0
		# 	while cur.elem != item:
		# 		count += 1
		# 		cur = cur.next

		# 	if count != 0:
		# 		while i < (count - 1):
		# 			i += 1
		# 			pre = pre.next
		# 		pre.next = cur.next
		# 	else:
		# 		self.__head = self.__head.next

	def search(self, item):
		"""查找节点是否存在"""

		cur = self.__head
		while cur is not None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False    


if __name__ == "__main__":
	sll = SingleLinkList()
	sll.append(1)
	sll.append(2)
	sll.append(3)
	sll.append(4)
	sll.append(5)
	sll.append(6)
	
	print(sll.length())