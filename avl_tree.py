'''avl tree'''
class Node:
    """
    Class representing a node in an AVL tree.
    Each node contains a value, pointers to left and right children,
    and the height of the node.
    """
    def __init__(self, value):
        """
        Initializes a node with a given value.
        The left and right children are set to None, and the height is set to 1.
        :param value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    Class representing an AVL tree.
    The AVL tree is a self-balancing binary search tree where the difference in heights
    between the left and right subtrees cannot be more than one for all nodes.
    """
    def __init__(self):
        """
        Initializes an empty AVL tree.
        """
        self.root = None

    def height(self, node):
        """
        Returns the height of the node.
        If the node is None, it returns 0.
        :param node: The node whose height is to be calculated.
        :return: The height of the node.
        """
        if not node:
            return 0
        return node.height

    def balance(self, node):
        """
        Balances the node by calculating the difference in heights
        between the left and right subtrees.
        :param node: The node to be balanced.
        :return: The difference in heights (left - right).
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        """
        Inserts a value into the AVL tree.
        The tree is balanced after the insertion.
        :param root: The root of the tree or subtree where the value is to be inserted.
        :param value: The value to be inserted.
        :return: The new root of the tree or subtree after insertion.
        """
        if not root:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        """
        Deletes a value from the AVL tree.
        The tree is balanced after the deletion.
        :param root: The root of the tree or subtree where the value is to be deleted.
        :param value: The value to be deleted.
        :return: The new root of the tree or subtree after deletion.
        """
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        """
        Rotates the subtree rooted at z to the left.
        This is used to balance the tree when the right subtree is taller.
        :param z: The root of the subtree to be rotated.
        :return: The new root of the subtree after rotation.
        """
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        """
        Rotates the subtree rooted at z to the right.
        This is used to balance the tree when the left subtree is taller.
        :param z: The root of the subtree to be rotated.
        :return: The new root of the subtree after rotation.
        """
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        """
        Calculates the node with the minimum value in the subtree rooted at root.
        This is used when deleting a node with two children.
        :param root: The root of the subtree.
        :return: The node with the minimum value in the subtree.
        """
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        """
        Searches for a value in the AVL tree.
        :param root: The root of the tree or subtree where the value is to be searched.
        :param value: The value to be searched.
        :return: The node containing the value if found, otherwise None.
        """
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def insert_value(self, value):
        """
        Inserts a value into the AVL tree.
        :param value: The value to be inserted.
        """
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        """
        Deletes a value from the AVL tree.
        :param value: The value to be deleted.
        """
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        """
        Searches for a value in the AVL tree.
        :param value: The value to be searched.
        :return: The node containing the value if found, otherwise None.
        """
        return self.search(self.root, value)

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the AVL tree.
        In-order traversal visits the left subtree, then the root, then the right subtree.
        :return: A list of values in in-order traversal order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        """
        Helper method for in-order traversal.
        :param root: The root of the tree or subtree.
        :param result: The list to store the traversal result.
        """
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.value)
            self._inorder_traversal(root.right, result)

    def preorder_traversal(self):
        """
        Performs a pre-order traversal of the AVL tree.
        Pre-order traversal visits the root, then the left subtree, then the right subtree.
        :return: A list of values in pre-order traversal order.
        """
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, root, result):
        """
        Helper method for pre-order traversal.
        :param root: The root of the tree or subtree.
        :param result: The list to store the traversal result.
        """
        if root:
            result.append(root.value)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)

    def postorder_traversal(self):
        """
        Performs a post-order traversal of the AVL tree.
        Post-order traversal visits the left subtree, then the right subtree, then the root.
        :return: A list of values in post-order traversal order.
        """
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, root, result):
        """
        Helper method for post-order traversal.
        :param root: The root of the tree or subtree.
        :param result: The list to store the traversal result.
        """
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.value)



def main():
    """
    Main function to demonstrate the AVL tree implementation.
    """
    avl_tree = AVLTree()

    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    print("Вставляємо елементи:", keys)
    for key in keys:
        avl_tree.insert_value(key)

    print("\nInorder обхід (відсортований порядок):", avl_tree.inorder_traversal())
    print("Preorder обхід (корінь, ліво, право):", avl_tree.preorder_traversal())
    print("Postorder обхід (ліво, право, корінь):", avl_tree.postorder_traversal())

    print("\nПошук елементів:")
    for key in [6, 15, 30]:
        result = avl_tree.search_value(key)
        if result:
            print(f"Елемент {key} знайдено")
        else:
            print(f"Елемент {key} не знайдено")

    print("\nВидалення елементів:")
    print("Видаляємо 20")
    avl_tree.delete_value(20)


    print("\nInorder обхід після видалення:", avl_tree.inorder_traversal())


if __name__ == '__main__':
    main()
