'''b tree'''
class BTreeNode:
    """
    A node in a B-tree.
    Each node contains a list of keys and a list of children.
    The node can be a leaf or an internal node.
    """
    def __init__(self, leaf=True):
        """
        Initializes a B-tree node.
        :param leaf: Boolean indicating if the node is a leaf node.
        """
        self.leaf = leaf
        self.keys = []
        self.children = []

    def display(self, level=0):
        """
        Displays the keys in the B-tree node.
        :param level: The level of the node in the tree (used for indentation).
        """
        print(f"Level {level}: {self.keys}")
        if not self.leaf:
            for child in self.children:
                child.display(level + 1)

class BTree:
    """
    A B-tree data structure.
    The B-tree is a self-balancing tree data structure that maintains sorted data
    and allows for efficient insertion, deletion, and search operations.
    """
    def __init__(self, t):
        """
        Initializes a B-tree with a given minimum degree (t).
        The minimum degree determines the range of children each node can have.
        :param t: Minimum degree of the B-tree.
        """
        self.root = BTreeNode(True)
        self.t = t

    def display(self):
        """
        Displays the B-tree structure starting from the root node.
        """
        self.root.display()

    def insert(self, k):
        """
        Inserts a new key into the B-tree.
        If the root node is full, it splits the root and creates a new root.
        :param k: The key to be inserted.
        """
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(leaf=False)
            self.root = temp
            temp.children.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        """
        Inserts a new key into a non-full node.
        This method is used when the node is not full and can accommodate the new key.
        :param x: The node where the key is to be inserted.
        :param k: The key to be inserted.
        """
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1

            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        """
        Splits a child node of a given node.
        This method is used when a child node is full and needs to be split into two nodes.
        :param x: The parent node where the child is to be split.
        :param i: The index of the child node to be split.
        """
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf=y.leaf)

        x.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        x.children.insert(i + 1, z)

# def main():
#     """
#     Main function to demonstrate the B-tree implementation.
#     """
#     b = BTree(3)

#     keys = [10, 20, 5, 6, 12, 30, 7, 17]
#     for key in keys:
#         b.insert(key)

#     print("B-tree structure:")
#     b.display()

# if __name__ == '__main__':
#     main()
