class Node:
    ''' Node that stores data and information about what it is linked to. '''
    def __init__(self, data=None):
        self.data = data
        self.prevnode = None
        self.nextnode = None

class DLL:
    ''' Double Linked List with some basic print functionality. '''
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        current_node = self.head
        while current_node is not None:
            if current_node.nextnode is None:
                end = '\n'
            else:
                end = '<->'
            print(current_node.data, end=end)
            current_node = current_node.nextnode
        print()

    def print_backwards(self):
        current_node = self.tail
        while current_node is not None:
            if current_node.prevnode is None:
                end = '\n'
            else:
                end = '<->'
            print(current_node.data, end=end)
            current_node = current_node.prevnode
        print()

    def delete_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prevnode is not None:
                    current_node.prevnode.nextnode = current_node.nextnode
                    break
                else:
                    self.head = current_node.nextnode
                    break
            else:
                current_node = current_node.nextnode

    def pop_front(self):
        to_pop = self.head
        self.head = to_pop.nextnode
        return to_pop

    def pop_back(self):
        to_pop = self.tail
        self.tail = to_pop.prevnode
        self.tail.nextnode = None
        return to_pop

    def kth_to_last(self, k):
        current_node = self.tail
        for count in range(k):
            if current_node.prevnode is not None:
                print(current_node.data)
                current_node = current_node.prevnode
            else:
                return False
        return current_node.data

print('Create a double linked list from elements Gabor')
l1 = DLL()
l1.head = Node('G')
n2 = Node('a')
n3 = Node('b')
n4 = Node('o')
n5 = Node('r')

l1.head.nextnode = n2
n2.prevnode = l1.head
n2.nextnode = n3
n3.prevnode = n2
n3.nextnode = n4
n4.prevnode = n3
n4.nextnode = n5
n5.prevnode = n4
l1.tail = n5

print('Print out the list')
l1.print()

print('Print out the list backwards')
l1.print_backwards()

print('{} to last element is {}'.format(3, l1.kth_to_last(3)))


print('Pop the first element from the list')
l1.pop_front()
l1.print()

print('Pop the last element from the list')
l1.pop_back()
l1.print()

print('Delete a data from the list (first occurance of "o")')
l1.delete_data('o')
l1.print()

        
