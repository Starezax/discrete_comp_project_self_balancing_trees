'''red black tree'''
class Node:
    """
    Class representing a node in a Red-Black Tree.
    Each node contains a key, color (red or black), and pointers to its parent, 
    left child, and right child.
    """
    def __init__(self, key, color='red'):
        """
        Initialize a node with a key and color.
        The default color is red.

        :param key: The key of the node
        :param color: The color of the node (red or black)
        """
        self.key = key
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    """
    Red-Black Tree implementation.
    This class provides methods for inserting, deleting, and searching for nodes,
    as well as performing in-order and pre-order traversals.
    """
    def __init__(self):
        """
        Initialize the Red-Black Tree with a sentinel NIL node.
        The NIL node is used to represent leaves and is always black.
        """
        self.NIL = Node(key=None, color='black')
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root = self.NIL

    def left_rotate(self, x):
        """
        Left rotate the subtree rooted at x.
        This operation is used during insertion and deletion to 
        maintain the Red-Black Tree properties.

        :param x: The node to be rotated
        :return: None
        """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
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

    def right_rotate(self, y):
        """
        Right rotate the subtree rooted at y.
        This operation is used during insertion and deletion to
        maintain the Red-Black Tree properties.

        :param y: The node to be rotated
        :return: None
        """
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, key):
        """
        Insert a new node with the given key into the Red-Black Tree.
        The new node is initially colored red and is inserted into the tree.
        The tree is then restructured and recolored to maintain the Red-Black properties.

        :param key: The key of the node to be inserted
        :return: None
        """
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = 'red'
        self.insert_fixup(node)

    def insert_fixup(self, z):
        """
        Insert fixup procedure to maintain the Red-Black Tree properties after insertion.
        This procedure ensures that the tree remains balanced and that the properties 
        of Red-Black Trees are satisfied.

        :param z: The newly inserted node
        :return: None
        """
        while z.parent and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'black'

    def transplant(self, u, v):
        """
        Transplant the subtree rooted at node u with the subtree rooted at node v.
        This operation is used during deletion to replace a node with its child.

        :param u: The node to be replaced
        :param v: The node to replace with
        :return: None
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        """
        Find the node with the minimum key in the subtree rooted at node.
        This is used during deletion to find the successor of a node.
        The minimum node is the leftmost node in the subtree.

        :param node: The root of the subtree
        :return: The node with the minimum key
        """
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, key):
        """
        Delete a node with the given key from the Red-Black Tree.
        The node is found and removed from the tree, and the tree is then restructured
        and recolored to maintain the Red-Black properties.

        :param key: The key of the node to be deleted
        :return: None
        """
        z = self.search_node(self.root, key)
        if z == self.NIL:
            return None
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.delete_fixup(x)

    def delete_fixup(self, x):
        """
        Delete fixup procedure to maintain the Red-Black Tree properties after deletion.
        This procedure ensures that the tree remains balanced and that the properties
        of Red-Black Trees are satisfied.

        :param x: The node to be fixed up after deletion
        :return: None
        """
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def search(self, key):
        """
        Search for a node with the given key in the Red-Black Tree.
        If the node is found, it is returned; otherwise, None is returned.

        :param key: The key to search for
        :return: The node with the given key or None if not found
        """
        node = self.search_node(self.root, key)
        return node if node != self.NIL else None

    def search_node(self, node, key):
        """
        Search for a node with the given key in the subtree rooted at node.
        This is a helper method used by the search method.

        :param node: The root of the subtree to search in
        :param key: The key to search for
        :return: The node with the given key or the NIL node if not found
        """
        while node != self.NIL and key != node.key:
            node = node.left if key < node.key else node.right
        return node

    def inorder_walk(self, node=None, res=None):
        """
        In-order traversal of the Red-Black Tree.
        This method returns the keys of the nodes in sorted order.

        :param node: The root of the subtree to traverse
        :param res: The list to store the keys in sorted order
        :return: A list of keys in sorted order
        """
        if res is None:
            res = []
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder_walk(node.left, res)
            res.append(node.key)
            self.inorder_walk(node.right, res)
        return res

    def preorder_walk(self, node=None, res=None):
        """
        Pre-order traversal of the Red-Black Tree.
        This method returns the keys of the nodes in pre-order.

        :param node: The root of the subtree to traverse
        :param res: The list to store the keys in pre-order
        :return: A list of keys in pre-order
        """
        if res is None:
            res = []
        if node is None:
            node = self.root
        if node != self.NIL:
            res.append(node.key)
            self.preorder_walk(node.left, res)
            self.preorder_walk(node.right, res)
        return res

if __name__ == "__main__":
    tree = RedBlackTree()
    values_to_insert = [20, 15, 25, 10, 5, 1, 30]
    print("Вставка елементів:", values_to_insert)
    for v in values_to_insert:
        tree.insert(v)
    print("In-order обхід після вставки:", tree.inorder_walk())
    print("Pre-order обхід після вставки:", tree.preorder_walk())

    print("\nПошук ключів 15 і 100:")
    print(tree.search(15))
    print(tree.search(100))

    print("\nВидалення ключів 15 і 100:")
    tree.delete(15)
    tree.delete(100)
    print("In-order обхід після видалення:", tree.inorder_walk())
    print("Pre-order обхід після видалення:", tree.preorder_walk())
