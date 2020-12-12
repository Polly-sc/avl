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

#поиск узлов в дереве
    def test_find_node(self):
        avl_tree = AVLTree()
        avl_tree.insert(2)
        node_2 = avl_tree.root
        avl_tree.insert(1)
        node_1 = avl_tree.root.left
        avl_tree.insert(4)
        node_4 = avl_tree.root.right
        avl_tree.insert(5)
        node_5 = node_4.right
        avl_tree.insert(9)
        node_9 = node_5.right
        avl_tree.insert(3)
        node_3 = node_4.left
        avl_tree.insert(6)
        node_6 = node_9.left
        avl_tree.insert(7)
        node_7 = node_5.right
        avl_tree.insert(15)
        node_15 = node_9.right

        self.assertEqual(avl_tree.search(5), node_5)
        self.assertEqual(avl_tree.search(2), node_2)
        self.assertEqual(avl_tree.search(1), node_1)
        self.assertEqual(avl_tree.search(4), node_4)
        self.assertEqual(avl_tree.search(3), node_3)
        self.assertEqual(avl_tree.search(7), node_7)
        self.assertEqual(avl_tree.search(6), node_6)
        self.assertEqual(avl_tree.search(9), node_9)
        self.assertEqual(avl_tree.search(15), node_15)
