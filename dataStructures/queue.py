# Making of queue data structure
class Queue:

	def __init__(self):
		self.item = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.item.pop()

	def size(self):
		return len(self.items)

		
