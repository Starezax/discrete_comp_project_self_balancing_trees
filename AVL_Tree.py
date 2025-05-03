"""
AVL Tree implementation
"""

class Node:
    """
    Represents a node in AVL Tree

    :attributes:
        key (int): The key stored in the node
        height (int): The height of the node
        left (Node | None): The left child of the node
        right (Node | None): The right child of the node
    """

    def __init__(self, key):
        """
        Initializes a new node with given key

        :param key: (int) the key data to store in the node
        """
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def update_height(self):
        """
        Updates the height of the node based on the heights of its children

        :returns: (Node) the updated node
        """
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)
        return self

    def balance_factor(self):
        """
        Calculates the balance factor of the node

        :returns: (int) the balance factor
        """
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def __repr__(self):
        """
        Returns a string representation of the node and its height

        :returns: (str)
        """
        return f"Node(key={self.key}, height={self.height})"


class AVLTree:
    """
    Represents an AVL Tree structure

    :attributes:
        root (Node | None): The root node of the tree
    """
    def __init__(self):
        """
        Initializes new AVL Tree instance with root None
        """
        self.root = None

    def _rotate_right(self, node):
        """
        Performs a right rotation on the subtree at param node.

        :param node: (Node) the root of the subtree to rotate
        :returns: (Node) the new root of the rotated subtree
        """
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.update_height()
        return left_child.update_height()

    def _rotate_left(self, node):
        """
        Performs a left rotation on the subtree at param node.

        :param node: (Node) the root of the subtree to rotate
        :returns: (Node) the new root of the rotated subtree
        """
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.update_height()
        return right_child.update_height()

    def _balance_subtree(self, node):
        """
        Balances the subtree rooted at param node by performing rotations if necessary.

        :param node: (Node | None) the root of the subtree to balance
        :returns: (Node | None) the balanced subtree root
        """
        if not node:
            return None
        node.update_height()
        factor = node.balance_factor()
        if factor > 1:
            if node.left and node.left.balance_factor() < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if factor < -1:
            if node.right and node.right.balance_factor() > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, key):
        """
        Inserts a key into the AVL Tree.

        :param key: (int) the key to insert
        :returns: None
        """
        def _insert(node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return self._balance_subtree(node)
        self.root = _insert(self.root, key)

    def delete(self, key):
        """
        Deletes a key from the AVL Tree.

        :param key: (int) the key to delete
        :returns: None
        """
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not (node.left and node.right):
                    return node.left or node.right
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.key, successor.key = successor.key, node.key
                node.right = _delete(node.right, successor.key)
            return self._balance_subtree(node)
        self.root = _delete(self.root, key)

    def search(self, key):
        """
        Searches for a key in the AVL Tree

        :param key: (int) the key to search for
        :returns: (bool) True if the key is found, False otherwise
        """
        def _search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            return _search(node.left, key) if key < node.key else _search(node.right, key)
        return _search(self.root, key)

    def pre_order(self):
        """
        Generator for preorder of tree

        :returns: (int) keys in pre-order
        """
        def _preorder(node):
            if node:
                yield node.key
                yield from _preorder(node.left)
                yield from _preorder(node.right)
        yield from _preorder(self.root)

    def in_order(self):
        """
        Generator for inorder of tree

        :returns: (int) keys in in-order
        """
        def _in_order(node):
            if node:
                yield from _in_order(node.left)
                yield node.key
                yield from _in_order(node.right)
        yield from _in_order(self.root)
