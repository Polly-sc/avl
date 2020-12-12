import unittest
from AVLtree import AVLTree, Node

class AVLtest(unittest.TestCase):
#инициализация дерева
    def test_tree_init(self):
        avl_tree = AVLTree()
        self.assertIsNone(avl_tree.root, None)

#инициализация узла дерева
    def test_node_init(self):
        node = Node(15)
        self.assertEqual(node.key, 15)
        self.assertTrue(node.red)
        self.assertIsNone(node.right, None)
        self.assertIsNone(node.left, None)
        self.assertIsNone(node.parent, None)

#вставка корня дерева
    def test_insert_root(self):
        avl_tree = AVLTree()
        avl_tree.insert(15)
        self.assertEqual(avl_tree.root.key, 15)
        self.assertEqual(avl_tree.root.key, 15)