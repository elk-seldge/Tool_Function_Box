class SNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class BNode:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None


class Singly_Linked_List:
	def __init__(self):
		self.head = None
		self.lngth = 0

	def length(self):
		return self.lngth

	def add(self, data):
		new_head = SNode(data)
		if not self.length():
			self.head = new_head
			print("none, add!")
			self.lngth += 1
			return 1
		else:
			self.head = new_head
			print("add!")
			self.lngth += 1
			return 1

	def append(self, data):
		new_tail = SNode(data)
		if not self.length():
			self.add(data)
			print("none, append!")
			return 1
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_tail
		print("append!")
		self.lngth += 1
		return 1


	def insert(self, data, pos):
		new_node = SNode(data)
		if not self.length():
			self.head =new_node
			self.lngth += 1
			print("none, insert")
			return 1
		elif pos > self.length():
			self.append(data)
			print("tail, insert!")
			self.lngth += 1
			return 1
		else:
			cur = self.head
			cntr = 0
			while cur.next != None:
				if cntr == pos-1:
					new_node.next = cur.next
					cur.next = new_node
					print("insert!")
					self.lngth += 1
					return 1
				cur = cur.next
				cntr += 1
		return None

	def delete(self, data):
		if not self.length():
			return 0
		else:
			cur = self.head
			while cur.next != None:
				if data == cur.next.data:
					cur.next = cur.next.next
					self.lngth -= 1
					return 1
				else:
					cur = cur.next
			return 0

	def traverse(self):
		if not self.length():
			return None
		else:
			cur = self.head
			while cur != None:
				print(cur.data)
				#yield cur.data
				cur = cur.next

	def search(self, data):
		if not self.length():
			return None
		else:
			cur = self.head
			cntr = 0
			while cur.next != None:
				if data == cur.data:
					return cntr
				else:
					cur = cur.next
					cntr += 1
			return None

	def head(self):
		return self.head

	def tail(self):
		cur = self.head
		while self.next != None:
				cur = cur.next
		return cur.data

class Doubly_Linked_List:
	def __init__(self):
		self.head = None
		self.lngth = 0

	def length(self):
		return self.lngth

	def add(self, data):
		new_head = BNode(data)
		if not self.length():
			self.head = new_head
			print("none, add!")
			self.lngth += 1
			return 1
		else:
			self.head.prev = new_head
			new_head.next = self.head
			self.head = new_head
			print("add!")
			self.lngth += 1
			return 1

	def append(self, data):
		new_tail = BNode(data)
		if not self.length():
			self.add(data)
			print("none, append!")
			return 1
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_tail
		new_tail.prev = cur
		print("append!")
		self.lngth += 1
		return 1


	def insert(self, data, pos):
		new_node = BNode(data)
		if not self.length():
			self.head =new_node
			self.lngth += 1
			print("none, insert")
			return 1
		elif pos > self.length():
			self.append(data)
			print("tail, insert!")
			self.lngth += 1
			return 1
		else:
			cur = self.head
			cntr = 0
			while cur.next != None:
				if cntr == pos-1:
					new_node.prev = cur
					new_node.next = cur.next
					cur.next.prev = new_node
					cur.next = new_node
					print("insert!")
					self.lngth += 1
					return 1
				cur = cur.next
				cntr += 1
		return None

	def delete(self, data):
		if not self.length():
			return 0
		else:
			cur = self.head
			while cur != None:
				if data == cur.data:
					cur.next.prev = cur.prev
					cur.prev.next = cur.next
					self.lngth -= 1
					return 1
				else:
					cur = cur.next
			return 0

	def traverse(self):
		if not self.length():
			return None
		else:
			cur = self.head
			while cur != None:
				print(cur.data)
				#yield cur.data
				cur = cur.next

	def search(self, data):
		if not self.length():
			return None
		else:
			cur = self.head
			cntr = 0
			while cur.next != None:
				if data == cur.data:
					return cntr
				else:
					cur = cur.next
					cntr += 1
			return None

	def head(self):
		return self.head

	def tail(self):
		cur = self.head
		while self.next != None:
				cur = cur.next
		return cur.data

class Circular_Singly_Linked_List:
	def __init__(self):
		self.head = None
		self.lngth = 0

	def length(self):
		return self.lngth

	def add(self, data):
		new_head = SNode(data)
		if not self.length():
			self.head = new_head
			new_head.next = self.head
			print("none, add!")
			self.lngth += 1
			return 1
		else:
			new_head.next = self.head
			self.head = new_head
			print("add!")
			self.lngth += 1
			return 1

	def append(self, data):
		new_tail = SNode(data)
		if not self.length():
			self.add(data)
			print("none, append!")
			return 1
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_tail
		print("append!")
		self.lngth += 1
		return 1


	def insert(self, data, pos):
		new_node = SNode(data)
		if not self.length():
			self.head =new_node
			self.lngth += 1
			print("none, insert")
			return 1
		elif pos > self.length():
			self.append(data)
			print("tail, insert!")
			self.lngth += 1
			return 1
		else:
			cur = self.head
			cntr = 0
			while cur.next != None:
				if cntr == pos-1:
					new_node.next = cur.next
					cur.next = new_node
					print("insert!")
					self.lngth += 1
					return 1
				cur = cur.next
				cntr += 1
		return None

	def delete(self, data):
		if not self.length():
			return 0
		else:
			cur = self.head
			while cur.next != None:
				if data == cur.next.data:
					cur.next = cur.next.next
					self.lngth -= 1
					return 1
				else:
					cur = cur.next
			return 0

	def traverse(self):
		if not self.length():
			return None
		else:
			cur = self.head
			while cur != None:
				print(cur.data)
				#yield cur.data
				cur = cur.next

	def search(self, data):
		if not self.length():
			return None
		else:
			cur = self.head
			cntr = 0
			while cur.next != None:
				if data == cur.data:
					return cntr
				else:
					cur = cur.next
					cntr += 1
			return None

	def head(self):
		return self.head

	def tail(self):
		cur = self.head
		while self.next != None:
				cur = cur.next
		return cur.data

