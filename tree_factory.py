'''tree factory'''
from tree_adapters import (
    AVLTreeAdapter,
    RedBlackTreeAdapter,
    SplayTreeAdapter,
    BTreeAdapter,
    TwoThreeTreeAdapter
)

class TreeFactory:
    """
    TreeFactory is a factory class that creates instances of different tree types.
    It provides a static method to create a tree based on the specified type.
    """
    @staticmethod
    def create_tree(tree_type):
        """
        Create a tree instance based on the specified tree type.
        The tree type can be one of the following:
        - "avl"
        - "red-black"
        - "splay"
        - "b-tree"
        - "2-3-tree"
        The tree type is case-insensitive.
        If an unknown tree type is specified, a ValueError is raised.
        """
        tree_type = tree_type.lower()

        if tree_type == "avl":
            return AVLTreeAdapter()
        if tree_type == "red-black":
            return RedBlackTreeAdapter()
        if tree_type == "splay":
            return SplayTreeAdapter()
        if tree_type == "b-tree":
            return BTreeAdapter(3)
        if tree_type == "2-3-tree":
            return TwoThreeTreeAdapter()
        raise ValueError(f"Unknown tree type: {tree_type}")
