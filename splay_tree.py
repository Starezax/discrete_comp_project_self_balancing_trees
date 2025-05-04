'''splay tree'''
class Node:
    """
    A class representing a node in a splay tree.
    Each node contains a key, pointers to its left and right children, and a pointer to its parent.
    """
    def __init__(self, key):
        """
        Initialize a node with a given key.
        The left and right children are initialized to None, 
        and the parent is also initialized to None.

        :param key: The key to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    """
    SplayTree is a class representing a splay tree data structure.
    A splay tree is a self-adjusting binary search tree with the additional property that
    recently accessed elements are quick to access again.
    It performs rotations to bring the accessed node to the root of the tree.
    """
    def __init__(self):
        """
        Initialize the SplayTree with a root node set to None.
        The tree starts empty, and nodes will be added through the insert method.
        The tree supports basic operations such as insertion, searching, and deletion.
        The tree also supports in-order and pre-order traversals.
        """
        self.root = None

    def rotate_left(self, x):
        """
        Rotate the subtree rooted at x to the left.
        This operation is used to maintain the properties of the splay tree.
        It moves the right child of x to be the new root of the subtree,
        and x becomes the left child of the new root.

        :param x: The node to be rotated left.
        :return: None
        """
        y = x.right
        if y is None:
            return

        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        """
        Rotate the subtree rooted at x to the right.
        This operation is used to maintain the properties of the splay tree.
        It moves the left child of x to be the new root of the subtree,
        and x becomes the right child of the new root.

        :param x: The node to be rotated right.
        :return: None
        """
        y = x.left
        if y is None:
            return

        x.left = y.right
        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, x):
        """
        Splay the node x to the root of the tree.
        This operation is performed by repeatedly rotating the node x
        until it becomes the root. The rotations are performed based on the
        position of x relative to its parent and grandparent.
        The splay operation is used to bring the accessed node closer to the root,
        making future accesses to that node faster.
        The splay operation is a key feature of splay trees, allowing them to adaptively
        reorganize themselves based on access patterns.

        :param x: The node to be splayed to the root.
        :return: None
        """
        while x.parent:
            if x.parent.parent is None:
                if x == x.parent.left:
                    self.rotate_right(x.parent)
                else:
                    self.rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.rotate_right(x.parent.parent)
                self.rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.rotate_left(x.parent.parent)
                self.rotate_left(x.parent)
            else:
                if x == x.parent.left:
                    self.rotate_right(x.parent)
                    self.rotate_left(x.parent)
                else:
                    self.rotate_left(x.parent)
                    self.rotate_right(x.parent)

    def subtree_minimum(self, x):
        """
        Search for the minimum node in the subtree rooted at x.
        This function traverses the left children of the nodes in the subtree
        until it reaches the leftmost node, which is the minimum node.
        The minimum node is the node with the smallest key in the subtree.
        This operation is used in the delete operation to find the successor of a node.
        The subtree_minimum function is a helper function that is used to find the minimum node
        in a subtree. It is particularly useful when deleting a node from the tree,
        as it helps to find the in-order successor of the node being deleted.

        :param x: The root of the subtree to search for the minimum node.
        :return: The node with the minimum key in the subtree.
        """
        while x.left:
            x = x.left
        return x

    def insert(self, key):
        """
        Insert a new node with the given key into the splay tree.
        If the key already exists, the node is splayed to the root.
        The insert operation first searches for the appropriate position to insert the new node.
        If the key is less than the current node's key, it moves to the left child.
        If the key is greater, it moves to the right child.
        If the key is equal to the current node's key, it means the key already exists in the tree,
        and the node is splayed to the root.
        If the appropriate position is found, a new node is created and inserted 
        as a child of the parent node.
        After insertion, the new node is splayed to the root of the tree.

        :param key: The key to be inserted into the tree.
        :return: None
        """
        node = self.root
        parent = None

        while node:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                self.splay(node)
                return

        new_node = Node(key)
        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.splay(new_node)

    def find(self, key):
        """
        Find a node with the given key in the splay tree.
        This function traverses the tree starting from the root and compares the keys.
        If the key is less than the current node's key, it moves to the left child.
        If the key is greater, it moves to the right child.
        If the key is equal to the current node's key, it returns the node.
        If the key is not found, it returns None.
        The find operation is used to search for a specific key in the tree.
        It is a standard binary search operation that traverses the 
        tree based on the key comparisons.

        :param key: The key to be searched in the tree.
        :return: The node with the given key, or None if not found.
        """
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def search(self, key):
        """
        Search for a node with the given key in the splay tree.
        This function first finds the node with the given key using the find method.
        If the node is found, it is splayed to the root of the tree.
        The search operation is similar to the find operation, but it also performs a splay
        operation on the found node to bring it to the root.
        This operation is useful when we want to access a node frequently,
        as it brings the node closer to the root for faster access in future operations.
        The search operation is a key feature of splay trees, allowing them to adaptively
        reorganize themselves based on access patterns.

        :param key: The key to be searched in the tree.
        :return: The node with the given key, or None if not found.
        """
        node = self.find(key)
        if node:
            self.splay(node)
        return node

    def delete(self, key):
        """
        Delete a node with the given key from the splay tree.
        This function first finds the node with the given key using the find method.
        If the node is found, it is splayed to the root of the tree.
        Then, the node is removed from the tree by adjusting the pointers of its children.
        If the node has a left child, the maximum node in the left subtree
        is found and splayed to the root.
        The right child of the maximum node is set to the right child of the deleted node.
        If the node has no left child, the right child of the deleted node is set as the new root.
        The delete operation is a standard binary search tree deletion operation,
        but it also performs a splay operation on the deleted node to bring it to the root.

        :param key: The key to be deleted from the tree.
        :return: None
        """
        node = self.find(key)
        if node is None:
            return

        self.splay(node)

        if node.left:
            left_subtree = node.left
            left_subtree.parent = None
        else:
            left_subtree = None

        if node.right:
            right_subtree = node.right
            right_subtree.parent = None
        else:
            right_subtree = None

        if left_subtree:
            max_node = self.subtree_minimum(left_subtree)
            self.splay(max_node)
            max_node.right = right_subtree
            if right_subtree:
                right_subtree.parent = max_node
            self.root = max_node
        else:
            self.root = right_subtree

    def inorder(self, node, res):
        """
        In-order traversal of the splay tree.
        This function traverses the tree in in-order fashion (left, root, right)
        and appends the keys of the nodes to the result list.
        The in-order traversal visits the nodes in ascending order of their keys.
        This operation is useful for obtaining a sorted list of keys in the tree.
        The inorder function is a recursive function that traverses the tree in in-order fashion.
        It starts from the root node and recursively visits the left subtree,
        then appends the key of the current node to the result list,
        and finally visits the right subtree.

        :param node: The root of the subtree to be traversed.
        :param res: The list to store the keys of the nodes in in-order.
        :return: None
        """
        if not node:
            return None
        self.inorder(node.left, res)
        res.append(node.key)
        self.inorder(node.right, res)

    def preorder(self, node, res):
        """
        Pre-order traversal of the splay tree.
        This function traverses the tree in pre-order fashion (root, left, right)
        and appends the keys of the nodes to the result list.
        The pre-order traversal visits the root node first, followed by the left subtree,
        and finally the right subtree.
        This operation is useful for obtaining a list of keys in the order they are visited.
        The preorder function is a recursive function that traverses the tree in pre-order fashion.
        It starts from the root node and appends the key of the current node to the result list,
        then recursively visits the left subtree, and finally visits the right subtree.

        :param node: The root of the subtree to be traversed.
        :param res: The list to store the keys of the nodes in pre-order.
        :return: None
        """
        if not node:
            return None
        res.append(node.key)
        self.preorder(node.left, res)
        self.preorder(node.right, res)
