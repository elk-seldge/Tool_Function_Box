class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()

	def top(self):
		return self.stack[-1] if not self.is_empty() else None

	def is_empty(self):
		return not self.stack

	def height(self):
		return len(self.stack) - 1

	def view(self):
		if self.is_empty():
			return []
		print("Bottom: \n")
		for item in self.stack:
			print(item)
		print("Top: \n")

class Queue():
	def __init__(self):
		self.queue = []

	def Enqueue(self, data):
		self.queue.append(data)

	def Dequeue(self):
		self.queue.pop(0)

	def is_empty(self):
		return not self.queue

	def length(self):
		return len(self.queue) - 1

	def view(self):
		if self.is_empty():
			return []
		print("Head: \n")
		for item in self.stack:
			print(item)
		print("Tail: \n")

class Dual_Queue():
	def __init__(self):
		self.queue = []

	def Enqueue_Head(self, data):
		self.queue.insert(0, data)

	def Enqueue_Tail(self, data):
		self.queue.append(data)

	def Dequeue_Head(self):
		self.queue.pop(0)

	def Dequeue_Tail(self):
		self.queue.pop()

	def is_empty(self):
		return not self.queue

	def length(self):
		return len(self.queue) - 1

	def view(self):
		if self.is_empty():
			return []
		for item in self.stack:
			print('Index: ', self.queue.index(item), 'Value: ', item)

