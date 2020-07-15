class Node(object):
	"""结点"""

	def __init__(self, item):
		self.elem = item
		self.next = None
		self.prev = None


class DoubleLinkList(object):
	"""双向链表"""

	def __init__(self, node = None):
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
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur != None:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")

	def add(self, item):
		"""链表头部添加结点，头插法"""
		node = Node(item)
		node.next = self.__head

		# self.__head.prev = node
		# self.__head = node
		self.__head = node
		node.next.prev = node


	def append(self, item):
		"""链表尾部添加结点，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur

	def insert(self, pos, item):
		"""指定位置添加结点
		param pos : 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			cur = self.__head
			count = 0
			while count < pos:
				count += 1
				cur = cur.next
			# 当退出循环后， cur 指向 pos 的位置
			node = Node(item)
			node.next = cur
			node.prev = cur.prev

			# cur.prev = node
			# node.prev.next = node
			cur.prev.next = node
			cur.prev = node

	def remove(self, item):
		"""删除结点"""
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				# 先判断此结点是否是头结点		
				# 头结点		
				if cur == self.__head:  
					self.__head = cur.next
					if cur.next:
						# 判断链表是否只有一个结点
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						# 判断是否是尾结点
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next


	def search(self, item):
		"""查找节点是否存在"""

		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False    


if __name__ == "__main__":

	dll = DoubleLinkList()

	dll.append(1)
	dll.append(2)
	dll.append(3)
	dll.travel()

	dll.insert(1, 4)
	dll.travel()