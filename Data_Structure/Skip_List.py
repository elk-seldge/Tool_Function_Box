import random


class Skip_Node():
	def	__init__(self, data=None, level = 10):
		self.data = data
		self.nexts = [None] * (level-1)

	def __str__(self):
		print("Data: ", self.data)

class Skip_List():
	def __init__(self, MAX_LEVEL):
		self.MAX_LEVEL = MAX_LEVEL
		self.head = Skip_Node(None, self.MAX_LEVEL)
		self.level = 0
		self.p = 0.25

	def Random_Level(self):
		lvl = 1
		while random.random() < self.p and lvl < self.MAX_LEVEL:
			lvl += 1
		return lvl

	def Check(self, data):
		if data == None:
			return -1
		else:
			cur = self.head
			# cntr = 0
			for i in range(self.level-1, -1, -1):
				while cur.nexts[i] and cur.nexts[i].data <= data:
					cur = cur.nexts[i]
					# cntr += 1
			return True if cur.data == data else False

	def Insert(self, data):
		if data == None:
			return -1
		else:
			updt = [None] * (self.max_level + 1)
			cur = self.head
			for i in range(self.level-1, -1, -1):
				while cur.nexts[i] and cur.nexts[i].data <= data:
					cur = cur.nexts[i]
				updt[i] = current
			if not cur.data or cur.data != data: # not found
				rlvl = self.Random_Level()
			if rlvl >= self.level:
				for i in range(self.level + 1, rlevel + 1):
					updt[i] = self.head
				self.level = rlvl
			new_node = Skip_Node(data, self.level)
			for i in range(self.level+1):
				new_node.nexts[i] = updt[i].nexts[i]
				updt[i].nexts[i] = new_node

	def Delete(self, data):
		if data == None:
			return -1
		else:
			updt = [None] * (self.max_level + 1)
			cur = self.head
			for i in range(self.level - 1, -1, -1):
				while cur.nexts[i] and cur.nexts[i].data <= data:
					cur = cur.nexts[i]
				updt[i] = current
			if not cur.data or cur.data != data:
				for i in range(self.level + 1):
					if updt[i].nexts[i] != cur:
						break
					updt[i].nexts[i] = cur.nexts[i]
				del current

				while self.level > 0 and self.head.nexts[self.level] is None:
					self.level -= 1

	def	View(self):
		cur = self.head
		for lvl in range(self.level + 1):
			print("Level {}: ".format(lvl))
			node = cur.nexts[lvl]
			while node is not None:
				print("Data: {}: ".format(node.data))
				node = node.nexts[lvl]
