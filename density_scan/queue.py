from linked_list import LinkedList

# Create Queue for use in density scanner
class MyQueue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size # return size of the queue

    def enqueue(self, value):
        # insert tail to the queue
        self.storage.add_to_tail(value)
        self.size += 1 # increment size of queue by 1

    def dequeue(self):
        if self.size > 0:  # check that there are items in the queue
            val = self.storage.remove_head()  # remove head of queue (first node) and store the value of the node removed
            self.size -= 1  # decrement the size by 1
            return val  # return value of the removed node
        return None  # if there is nothing in the queue, return None