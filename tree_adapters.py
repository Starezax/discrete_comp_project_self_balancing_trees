'''tree adapters'''
from abstract_class import SelfBalancingTree
from AVL_Tree import AVLTree
from red_black_tree import RedBlackTree
from splay_tree import SplayTree
from b_tree import BTree
from two_three_tree import TwoThreeTree

class AVLTreeAdapter(SelfBalancingTree):
    """
    Adapter class for AVL Tree that implements the SelfBalancingTree interface.
    This class provides methods for inserting, deleting, searching, and traversing the AVL Tree.
    The AVL Tree is a self-balancing binary search tree.
    It maintains its balance by ensuring that the heights of the two child subtrees 
    of any node differ by at most one.
    """
    def __init__(self):
        """
        Initialize the AVLTreeAdapter with an instance of AVLTree.
        The AVLTree is a self-balancing binary search tree.
        """
        self.tree = AVLTree()

    def insert(self, key):
        """
        Insert a key into the AVL Tree.
        The key is inserted in a way that maintains the AVL Tree properties.
        
        :param key: The key to be inserted into the AVL Tree.
        :return: None
        """
        self.tree.insert(key)

    def delete(self, key):
        """
        Delete a key from the AVL Tree.
        The key is deleted in a way that maintains the AVL Tree properties.

        :param key: The key to be deleted from the AVL Tree.
        :return: None
        """
        self.tree.delete(key)

    def search(self, key):
        """
        Search for a key in the AVL Tree.
        The method returns True if the key is found, otherwise False.

        :param key: The key to be searched in the AVL Tree.
        :return: bool - True if the key is found, otherwise False.
        """
        return self.tree.search(key)

    def inorder_traversal(self):
        """
        In-order traversal of the AVL Tree.
        The method returns a list of keys in sorted order.

        :return: list - A list of keys in sorted order.
        """
        return list(self.tree.in_order())

    def preorder_traversal(self):
        """
        Pre-order traversal of the AVL Tree.
        The method returns a list of keys in pre-order.

        :return: list - A list of keys in pre-order.
        """
        return list(self.tree.pre_order())

    def is_empty(self):
        """
        Check if the AVL Tree is empty.
        The method returns True if the tree is empty, otherwise False.

        :return: bool - True if the tree is empty, otherwise False.
        """
        return self.tree.root is None

class RedBlackTreeAdapter(SelfBalancingTree):
    """
    Adapter class for Red-Black Tree that implements the SelfBalancingTree interface.
    This class provides methods for inserting, deleting, searching, 
    and traversing the Red-Black Tree.
    """
    def __init__(self):
        """
        Initialize the RedBlackTreeAdapter with an instance of RedBlackTree.
        The RedBlackTree is a self-balancing binary search tree.
        """
        self.tree = RedBlackTree()

    def insert(self, key):
        """
        Insert a key into the Red-Black Tree.
        The key is inserted in a way that maintains the Red-Black Tree properties.

        :param key: The key to be inserted into the Red-Black Tree.
        :return: None
        """
        self.tree.insert(key)

    def delete(self, key):
        """
        Delete a key from the Red-Black Tree.
        The key is deleted in a way that maintains the Red-Black Tree properties.

        :param key: The key to be deleted from the Red-Black Tree.
        :return: None
        """
        self.tree.delete(key)

    def search(self, key):
        """
        Search for a key in the Red-Black Tree.
        The method returns True if the key is found, otherwise False.

        :param key: The key to be searched in the Red-Black Tree.
        :return: bool - True if the key is found, otherwise False.
        """
        return self.tree.search(key) is not None

    def inorder_traversal(self):
        """
        In-order traversal of the Red-Black Tree.
        The method returns a list of keys in sorted order.

        :return: list - A list of keys in sorted order.
        """
        return self.tree.inorder_walk()

    def preorder_traversal(self):
        """
        Pre-order traversal of the Red-Black Tree.
        The method returns a list of keys in pre-order.

        :return: list - A list of keys in pre-order.
        """
        return self.tree.preorder_walk()

    def is_empty(self):
        """
        Check if the Red-Black Tree is empty.
        The method returns True if the tree is empty, otherwise False.

        :return: bool - True if the tree is empty, otherwise False.
        """
        return self.tree.root == self.tree.NIL

class SplayTreeAdapter(SelfBalancingTree):
    """
    Adapter class for Splay Tree that implements the SelfBalancingTree interface.
    This class provides methods for inserting, deleting, searching,
    and traversing the Splay Tree.
    The Splay Tree is a self-adjusting binary search tree.
    """
    def __init__(self):
        """
        Initialize the SplayTreeAdapter with an instance of SplayTree.
        The SplayTree is a self-adjusting binary search tree.
        """
        self.tree = SplayTree()

    def insert(self, key):
        """
        Insert a key into the Splay Tree.
        The key is inserted in a way that maintains the Splay Tree properties.

        :param key: The key to be inserted into the Splay Tree.
        :return: None
        """
        self.tree.insert(key)

    def delete(self, key):
        """
        Delete a key from the Splay Tree.
        The key is deleted in a way that maintains the Splay Tree properties.
        The method first splays the key to the root and then deletes it.

        :param key: The key to be deleted from the Splay Tree.
        :return: None
        """
        self.tree.delete(key)

    def search(self, key):
        """
        Search for a key in the Splay Tree.
        The method returns True if the key is found, otherwise False.

        :param key: The key to be searched in the Splay Tree.
        :return: bool - True if the key is found, otherwise False.
        """
        return self.tree.search(key) is not None

    def inorder_traversal(self):
        """
        In-order traversal of the Splay Tree.
        The method returns a list of keys in sorted order.

        :return: list - A list of keys in sorted order.
        """
        result = []
        self.tree.inorder(self.tree.root, result)
        return result

    def preorder_traversal(self):
        """
        Pre-order traversal of the Splay Tree.
        The method returns a list of keys in pre-order.

        :return: list - A list of keys in pre-order.
        """
        result = []
        self.tree.preorder(self.tree.root, result)
        return result

    def is_empty(self):
        """
        Check if the Splay Tree is empty.
        The method returns True if the tree is empty, otherwise False.

        :return: bool - True if the tree is empty, otherwise False.
        """
        return self.tree.root is None

class BTreeAdapter(SelfBalancingTree):
    """
    Adapter class for B-Tree that implements the SelfBalancingTree interface.
    This class provides methods for inserting, deleting, searching,
    and traversing the B-Tree.
    The B-Tree is a self-balancing tree data structure that maintains sorted data
    and allows searches, sequential access, insertions, and deletions in logarithmic time.
    """
    def __init__(self, degree=3):
        """
        Initialize the BTreeAdapter with an instance of BTree.
        The BTree is a self-balancing tree data structure.
        The degree of the B-Tree determines the maximum number of children each node can have.
        The default degree is set to 3.

        :param degree: int - The degree of the B-Tree (default is 3).
        """
        self.tree = BTree(degree)

    def insert(self, key):
        """
        Insert a key into the B-Tree.
        The key is inserted in a way that maintains the B-Tree properties.

        :param key: The key to be inserted into the B-Tree.
        :return: None
        """
        self.tree.insert(key)

    def delete(self, key):
        """
        Delete a key from the B-Tree.
        The key is deleted in a way that maintains the B-Tree properties.

        :param key: The key to be deleted from the B-Tree.
        :return: None
        """
        self.tree.delete(key)

    def search(self, key):
        """
        Search for a key in the B-Tree.
        The method returns True if the key is found, otherwise False.

        :param key: The key to be searched in the B-Tree.
        :return: bool - True if the key is found, otherwise False.
        """
        return self.tree.search(key) is not None

    def inorder_traversal(self):
        """
        In-order traversal of the B-Tree.
        The method returns a list of keys in sorted order.

        :return: list - A list of keys in sorted order.
        """
        return self.tree.inorder_traversal()

    def preorder_traversal(self):
        """
        Pre-order traversal of the B-Tree.
        The method returns a list of keys in pre-order.

        :return: list - A list of keys in pre-order.
        """
        return self.tree.preorder_traversal()

    def is_empty(self):
        """
        Check if the B-Tree is empty.
        The method returns True if the tree is empty, otherwise False.

        :return: bool - True if the tree is empty, otherwise False.
        """
        return self.tree.root is None or len(self.tree.root.keys) == 0

class TwoThreeTreeAdapter(SelfBalancingTree):
    """
    Adapter class for 2-3 Tree that implements the SelfBalancingTree interface.
    This class provides methods for inserting, deleting, searching,
    and traversing the 2-3 Tree.
    The 2-3 Tree is a balanced search tree where every node can have either 2 or 3 children.
    It maintains sorted data and allows searches, sequential access, insertions, and 
    deletions in logarithmic time.
    """
    def __init__(self):
        """
        Initialize the TwoThreeTreeAdapter with an instance of TwoThreeTree.
        The TwoThreeTree is a balanced search tree.
        """
        self.tree = TwoThreeTree()

    def insert(self, key):
        """
        Insert a key into the 2-3 Tree.
        The key is inserted in a way that maintains the 2-3 Tree properties.

        :param key: The key to be inserted into the 2-3 Tree.
        :return: None
        """
        self.tree.insert(key)

    def delete(self, key):
        """
        Delete a key from the 2-3 Tree.
        The key is deleted in a way that maintains the 2-3 Tree properties.

        :param key: The key to be deleted from the 2-3 Tree.
        :return: None
        """
        self.tree.delete(key)

    def search(self, key):
        """
        Search for a key in the 2-3 Tree.
        The method returns True if the key is found, otherwise False.

        :param key: The key to be searched in the 2-3 Tree.
        :return: bool - True if the key is found, otherwise False.
        """
        return self.tree.search(key)

    def inorder_traversal(self):
        """
        In-order traversal of the 2-3 Tree.
        The method returns a list of keys in sorted order.

        :return: list - A list of keys in sorted order.
        """
        return self.tree.inorder_traversal()

    def preorder_traversal(self):
        """
        Pre-order traversal of the 2-3 Tree.
        The method returns a list of keys in pre-order.

        :return: list - A list of keys in pre-order.
        """
        return self.tree.preorder_traversal()

    def is_empty(self):
        """
        Check if the 2-3 Tree is empty.
        The method returns True if the tree is empty, otherwise False.

        :return: bool - True if the tree is empty, otherwise False.
        """
        return self.tree.root is None or not self.tree.root.keys
