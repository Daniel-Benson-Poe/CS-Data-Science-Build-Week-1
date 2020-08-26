# Node class for use in linked list
class Node:

    def __init__(self, value, next_node=None):
        # Value the node is holding
        self.value = value
        # reference to the next node
        self.next_node = next_node

    # method to get value of the node
    def get_value(self):
        return self.value

    # method to get the node's next node
    def get_next(self):
        return self.next_node

    # method to update the node's next node to the input node
    def set_next(self, new_next):
        self.next_node = new_next

# Create class for linked list
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap value in a node
        new_node = Node(value)
        # check if linked list is empty
        if self.head is None and self.tail is None:
            # set head and tail to new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list has at least one node
        else:
            # update last node's next node to the new node
            self.tail.set_next(new_node)
            # update self.tail to point to the new node 
            self.tail = new_node

    def remove_tail(self):
        # Check if linked list is empty
        if self.head is None and self.tail is None:
            return None

        # check if linked list has only one node
        if self.head == self.tail:
            # store the value of the node we are going to remove
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise linked list has more than one node
        else:
            # store that node's value in another variable
            val = self.tail.get_value()
            # need to set 'self.tail' to second-to-last node
            # only way is by traversing the whole linked list from the beginning

            # starting from the head, we'll traverse down to the second to last node
            # init another reference to keep track of where we are in the linked list
            # as we're iterating
            current = self.head
            # keep iterating until the node after current is the tail
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()
            # set tail to current
            self.tail = current
            # set new tail's next node to none
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one node in linked list
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value
            val = self.head.get_value()
            # set head to old head's next node
            self.head = self.head.get_next()
            # return the old head's value
            return val
