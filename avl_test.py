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

#вставка узлов дерева
    def test_Insert(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(10)

        self.assertFalse(tree.root)
        self.assertFalse(tree.search(15))
        self.assertFalse(tree.search(25))
        tree.insert(17)
        tree.insert(8)
        self.assertTrue(tree.search(15))
        self.assertFalse(tree.search(10))
        self.assertFalse(tree.search(17))
        self.assertTrue(tree.search(8))
        tree.insert(9)
        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(8))
        self.assertEqual(tree.search(9).left.key, 8)

#нахождение следующего узла дерева (правый сын)
    def test_Next(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        node1 = tree.root.right
        tree.insert(10)
        tree.insert(30)
        node2 = node1.right

        self.assertIsNone(tree.FindNext(15))
        self.assertEqual(tree.FindNext(20), node1)
        self.assertEqual(tree.FindNext(25), node2)

#нахождение предыдущего узла дерева (левый сын)
    def test_Prev(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        node1 = tree.root.left
        tree.insert(10)
        node2 = node1.left

        self.assertIsNone(tree.FindPrev(25))
        self.assertEqual(tree.FindPrev(20), node1)
        self.assertEqual(tree.FindPrev(15), node2)

# удаление корня дерева
    def test_root_delete(self):
        tree = AVLTree()
        root = Node(5)
        left_child = Node(3)
        left_child.parent = root
        left_child.left = Node(None)
        left_child.right = Node(None)
        right_child = Node(8)
        right_child.parent = root
        right_child.left = Node(None)
        right_child.right = Node(None)
        root.left = left_child
        root.right = right_child
        tree.root = root
        tree.deleteNode(5)

        self.assertEqual(tree.root.key, 8)
        self.assertEqual(tree.root.left.key, 3)


    def test_delete_left_node_noChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        node = tree.root.left
        tree.delete_left_node_noChildren(node)
        self.assertIsNone(tree.root.left.key)


    def test_delete_left_node_onlyRightChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(17)
        node = tree.root.left
        tree.delete_left_node_onlyRightChildren(node)
        self.assertEqual(tree.root.left.key, 17)

    def test_delete_left_node_onlyLeftChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(14)
        node = tree.root.left
        tree.delete_left_node_onlyLeftChildren(node)
        self.assertEqual(tree.root.left.key, 14)


    def test_delete_left_node_bothChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(14)
        tree.insert(18)
        node = tree.root.left
        tree.delete_left_node_onlyLeftChildren(node)
        self.assertEqual(tree.root.left.key, 14)


    def test_delete_right_node_noChildren(self):
        tree = AVLTree()
        tree.insert(15)
        tree.insert(20)
        tree.insert(25)
        node = tree.root.right
        tree.delete_right_node_noChildren(node)
        self.assertIsNone(tree.root.right.key)


    def test_delete_right_node_onlyRightChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(30)
        node = tree.root.right
        tree.delete_right_node_onlyRightChildren(node)
        self.assertEqual(tree.root.right.key, 30)


    def test_delete_right_node_onlyLeftChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(23)
        node = tree.root.right
        tree.delete_right_node_onlyLeftChildren(node)
        self.assertEqual(tree.root.right.key, 23)


    def test_delete_right_node_bothChildren(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(23)
        tree.insert(30)
        node = tree.root.right
        tree.delete_right_node_bothChildren(node)
        self.assertEqual(tree.root.right.key, 30)

    # удаление узлов дерева
    def test_Delete(self):
        tree = AVLTree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(23)
        tree.insert(27)
        self.assertEqual(tree.root.right.key, 25)
        self.assertEqual(tree.root.right.left.key, 23)
        tree.deleteNode(25)
        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.root.right.key, 27)
        self.assertIsNone(tree.root.right.right.key, None)
        self.assertEqual(tree.root.right.left.key, 23)
           