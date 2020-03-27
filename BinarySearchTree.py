class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        inserts value at appropriate parent
        :param value: value to be inserted
        :return: leave function
        """
        #Empty Tree then we set root node
        if self.root is None:
            new_node = Node(value, None, None, None)
            self.root = new_node
            self.size += 1
            return
        node_search = self.search(value, self.root)
        if node_search.value == value:
            return
        #find correct leaf for insertion by traversing tree
        else:
            current = self.root
            while current is not None:
                if value < current.value:
                    if current.left is None:
                        new_node = Node(value, current, None, None)
                        current.left = new_node
                        self.size += 1
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        new_node = Node(value, current, None, None)
                        current.right = new_node
                        self.size += 1
                        return
                    else:
                        current = current.right

    def remove(self, value):
        """
        remove value and adjust children appropriately
        :param value: value to be removed
        :return: None
        """
        parent = None
        current_node = self.root
        if self.size == 1:
            self.root = None
            self.size = 0
            return None
        # Search for the node.
        while current_node is not None:
            # Check if current_node has a matching key.
            if current_node.value == value:
                if current_node.left is None and current_node.right is None:   # Case 1
                    if parent is None: # Node is root
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    self.size -= 1
                    return None # Node found and removed
                elif current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    self.size -= 1
                    return None  # Node found and removed
                elif current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    self.size -= 1
                    return None  # Node found and removed
                else:                                    # Case 3
                    # Find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.value = successor.value      # Copy successor to current node
                    parent = current_node
                    current_node = current_node.right     # Remove successor from right subtree
                    value = parent.value  # Loop continues with new key
            elif current_node.value < value: # Search right
                parent = current_node
                current_node = current_node.right
            else:                        # Search left
                parent = current_node
                current_node = current_node.left
        return None

    def search(self, value, node):
        """
        search the tree for the value parameter
        :param value: value to be removed
        :param node: root of given tree or subtree
        :return: node
        """
        if node is None:
            return None
        if value == node.value:
            return node
        else:
            if value < node.value and node.left is not None:
                return self.search(value, node.left)
            elif value > node.value and node.right is not None:
                return self.search(value, node.right)
        return node

    def inorder(self, node):
        """
        traverse the tree inorder
        :param node: node to begin traversal
        :yield: value at each node
        """
        if node:
            for value in self.inorder(node.left):
                yield value
            yield node.value
            for value in self.inorder(node.right):
                yield value
    def preorder(self, node):
        """
        traverse the tree preorder
        :param node: node to begin traversal
        :yield: value at each node
        """
        if node:
            yield node.value
            for value in self.preorder(node.left):
                yield value
            for value in self.preorder(node.right):
                yield value
                
    def postorder(self, node):
        """
        traverse the tree postorder
        :param node: node to begin traversal
        :yield: value at each node
        """
        if node:
            for value in self.postorder(node.left):
                yield value
            for value in self.postorder(node.right):
                yield value
            yield node.value

    def depth(self, value):
        """
        returns the depth of the node with the provided value
        :param value: value to find depth of in tree
        :return: depth of node with given value
        """
        if value is None or self.root is None:
            return -1
        nodel = self.search(value, self.root)
        if nodel is None:
            return -1
        if nodel.value != value:
            return -1
        if nodel.value == self.root.value:
            return 0
        else:
            nodel.value = nodel.parent.value
            return 1 + self.depth(nodel.value)
        
    def height(self, node):
        """
        return height of the tree at provided node
        :param node: node to find height from
        :return: height of tree from node
        """
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def min(self, node):
        """
        returns node with minimum value in tree
        :param node: root to begin traversal
        :return: minimum value
        """
        if node is None:
            return None
        if node.left != None:
            return self.min(node.left)
        else:
            res = node
            return res

    def max(self, node):
        """
        returns node with maximum value in tree
        :param node: root to begin traversal
        :return: maximum value
        """
        if node is None:
            return None
        if node.right is not None:
            return self.max(node.right)
        else:
            res = node
            return res
        
    def get_size(self):
        """
        returns the amount of nodes in tree
        :return: size of tree
        """
        return self.size

    def is_perfect(self, node):
        """
        checks if tree rooted at given node is perfect
        :param node: node to start test at 
        :return: True or False
        """
        height = self.height(node)
        comparison = 2**(height +1) - 1
        if comparison == self.size:
            return True
        else:
            return False

    def is_degenerate(self):
        """
        return a boolean if tree is degenerate
        :return: True or False
        """
        i = 0
        current = self.root 
        if self.size == 0:
            return False
        if self.is_perfect == True:
            return False
        while i < self.size:
            if current.left is not None:
                if current.right is not None:
                    return False
                else:
                    current = current.left
                    i += 1
            else:
                if current.right is not None:
                    current = current.right
                    i += 1
                else:
                    return True  
                    