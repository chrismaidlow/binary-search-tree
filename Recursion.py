"""
PROJECT 2 - Recursion
Name: Chris Maidlow
PID: A49592527
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """insert node into list"""
    #If the LinkedList is empty
    if node is None:
        new_node = LinkedNode(value, None)
        return new_node
    #If head is more than value
    elif node.value >= value:
        new_node = LinkedNode(value, None)
        new_node.next_node = node
        return new_node
    #iterating through list
    elif node.value < value:
        node.next_node = insert(value, node.next_node)
        return node

def string(node):
    """return the list as a string"""
    ret_str = ""
    # if list is empty
    if node is None:
        ret_str = ""
        return ret_str
    elif node.next_node is None:
        ret_str += str(node.value)
        return ret_str
    else:
        ret_str = str(node.value) + ", "
        ret_str += string(node.next_node)
        return ret_str
    # iterate through list
def reversed_string(node):
    pass
def remove(value, node):
    """remove node from linkedlist"""
    if node is None:
        return None
    if value == node.value:
        node = node.next_node
        return node
    elif node.next_node.next_node is None:
        if value == node.next_node.value:
            node.next_node = None
            return node
        else:
            return node
    elif value == node.next_node.value:
        node.next_node = (node.next_node).next_node
        return node
    else:
        node.next_node = remove(value, node.next_node)
        return node
def remove_all(value, node):
    """remove all nodes with certain value"""
    #if empty
    if node is None:
        return None
    #if head is item to be removed
    if value == node.value:
        node = node.next_node
    #upon arriving at 2nd to last node
    elif node.next_node.next_node is None:
        if value == node.next_node.value:
            node.next_node = None
            return node
        else:
            return node
    elif value == node.next_node.value:
        node.next_node = (node.next_node).next_node
        remove_all(value, node)
    else:
        remove_all(value, node.next_node)
def search(value, node):
    """search linkedlist for node"""
    if node is None:
        return False
    else:
        if value == node.value:
            return True
        elif value != node.value:
            return search(value, node.next_node)
def length(node):
    """return the length of the list"""
    if node is None:
        return 0
    leng = 0
    if node.next_node is None:
        leng += 1
        return leng
    else:
        leng += 1
        leng += length(node.next_node)
        return leng 
def sum_all(node):
    """sum the values of all nodes"""
    total = 0
    if node is None:
        total = 0
        return total
    elif node.next_node is None:
        total += node.value
        return total
    else:
        total = node.value
        total += sum_all(node.next_node)
        return total
def count(value, node):
    """count the amount of nodes with value in list"""
    counter = 0
    if node is None:
        counter = 0
        return counter
    elif node.next_node is None:
        if value == node.value:
            counter += 1
            return counter
        else:
            return counter
    else:
        if value == node.value:
            counter += 1
            counter += count(value, node.next_node)
            return counter
        if value != node.value:
            counter += count(value, node.next_node)
            return counter