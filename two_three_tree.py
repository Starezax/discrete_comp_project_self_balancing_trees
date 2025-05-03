'''2-3 tree'''
class Node:
    """
    Class for representing a node in a 2-3 tree.
    """
    def __init__(self):
        self.keys = []
        self.children = []
        self.is_leaf = True

    def is_full(self):
        """
        Checks if the node is full (has 2 keys).
        """
        return len(self.keys) == 2


class TwoThreeTree:
    """
    Represents a 2-3 tree data structure.
    Supports insertion, deletion, and searching for keys.
    """
    def __init__(self):
        """
        Creates an empty 2-3 tree.
        """
        self.root = None

    def search(self, key):
        """
        Searches for a key in the tree.
        Returns True if found, False otherwise.
        :param key: The key to search for.
        :return: True if the key is found, False otherwise.
        """
        if not self.root:
            return False

        return self._search(self.root, key)

    def _search(self, node, key):
        """
        Helper method to search for a key in the tree recursively.
        :param node: The current node being searched.
        :param key: The key to search for.
        :return: True if the key is found, False otherwise.
        """
        if key in node.keys:
            return True

        if node.is_leaf:
            return False

        if key < node.keys[0]:
            return self._search(node.children[0], key)
        elif len(node.keys) == 1 or key < node.keys[1]:
            return self._search(node.children[1], key)
        else:
            return self._search(node.children[2], key)

    def insert(self, key):
        """
        Inserts a key into the tree.
        :param key: The key to insert.
        """
        if not self.root:
            self.root = Node()
            self.root.keys.append(key)
            return

        if len(self.root.keys) == 2 and self._insert_in_node(self.root, key) == -1:
            old_root = self.root
            self.root = Node()
            self.root.is_leaf = False

            middle_key = old_root.keys[1]
            self.root.keys.append(middle_key)

            left_node = Node()
            left_node.keys.append(old_root.keys[0])
            left_node.is_leaf = old_root.is_leaf

            right_node = Node()
            right_node.keys.append(old_root.keys[2])
            right_node.is_leaf = old_root.is_leaf

            if not old_root.is_leaf:
                left_node.children.append(old_root.children[0])
                left_node.children.append(old_root.children[1])
                right_node.children.append(old_root.children[2])
                right_node.children.append(old_root.children[3])

            self.root.children.append(left_node)
            self.root.children.append(right_node)

            if key < middle_key:
                self._insert_in_node(left_node, key)
            else:
                self._insert_in_node(right_node, key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """
        Recursively inserts a key into the tree. 
        :param node: The current node being processed.
        :param key: The key to insert.
        """
        if node.is_leaf:
            self._insert_in_node(node, key)
            return

        child_index = 0
        if len(node.keys) == 1:
            if key >= node.keys[0]:
                child_index = 1
        else:
            if key >= node.keys[1]:
                child_index = 2
            elif key >= node.keys[0]:
                child_index = 1

        child = node.children[child_index]

        if len(child.keys) == 2 and self._insert_in_node(child, key) == -1:
            middle_key = child.keys[1]

            new_node = Node()
            new_node.keys.append(child.keys[2])
            new_node.is_leaf = child.is_leaf

            child.keys = [child.keys[0]]

            if not child.is_leaf:
                new_node.children.append(child.children[2])
                new_node.children.append(child.children[3])
                child.children = [child.children[0], child.children[1]]

            pos = self._insert_in_node(node, middle_key)

            node.children.insert(pos + 1, new_node)

            if key < middle_key:
                self._insert_in_node(child, key)
            else:
                self._insert_in_node(new_node, key)
        else:

            self._insert_recursive(child, key)

    def _insert_in_node(self, node, key):
        """
        Inserts a key into a node.
        :param node: The node to insert the key into.
        :param key: The key to insert.
        :return: The position where the key was inserted, or -1 if the node is full.
        """

        if key in node.keys:
            return node.keys.index(key)

        if len(node.keys) == 3:
            return -1

        pos = 0
        while pos < len(node.keys) and key > node.keys[pos]:
            pos += 1

        node.keys.insert(pos, key)
        return pos

    def delete(self, key):
        """
        Deletes a key from the tree.
        :param key: The key to delete.
        """
        if not self.root:
            return

        if not self.search(key):
            return

        self._delete_recursive(self.root, key)

        if not self.root.keys:
            if self.root.children:
                self.root = self.root.children[0]
            else:
                self.root = None

    def _delete_recursive(self, node, key):
        """
        Deletes a key from the tree recursively.
        :param node: The current node being processed.
        :param key: The key to delete.
        """

        if key in node.keys:
            key_index = node.keys.index(key)

            if node.is_leaf:
                node.keys.pop(key_index)
            else:
                successor = self._find_min(node.children[key_index + 1])

                node.keys[key_index] = successor

                self._delete_recursive(node.children[key_index + 1], successor)
        else:
            if node.is_leaf:
                return

            child_index = 0
            if len(node.keys) == 1:
                if key >= node.keys[0]:
                    child_index = 1
            else:
                if key >= node.keys[1]:
                    child_index = 2
                elif key >= node.keys[0]:
                    child_index = 1

            self._delete_recursive(node.children[child_index], key)

    def _find_min(self, node):
        """
        Finds the minimum key in a subtree rooted at the given node.
        :param node: The root of the subtree.
        """
        current = node
        while not current.is_leaf:
            current = current.children[0]

        return current.keys[0]

    def inorder_traversal(self):
        """
        Do in-order traversal of the tree.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """
        Helper method for in-order traversal of the tree.
        :param node: The current node being processed.
        """
        if not node:
            return

        if node.is_leaf:
            result.extend(node.keys)
            return

        self._inorder_traversal(node.children[0], result)

        result.append(node.keys[0])

        self._inorder_traversal(node.children[1], result)

        if len(node.keys) > 1:
            result.append(node.keys[1])
            self._inorder_traversal(node.children[2], result)

    def preorder_traversal(self):
        """
        Do pre-order traversal of the tree.
        """
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        """
        Helper method for pre-order traversal of the tree.
        :param node: The current node being processed.
        :param result: The list to store the traversal result.
        """
        if not node:
            return

        result.extend(node.keys)

        if not node.is_leaf:
            for child in node.children:
                self._preorder_traversal(child, result)
