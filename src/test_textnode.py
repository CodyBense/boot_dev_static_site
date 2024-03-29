import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node3 = TextNode("This is a secondary text node", "bold")
        node4 = TextNode("This is a secondary text node", "none")
        self.assertEqual(node3, node4)

    def test_eq_false2(self):
        node5 = TextNode("This is a third text node", "bold")
        node6 = TextNode("This is a fourth text node", "bold")
        self.assertEqual(node5, node6)

    def test_eq_false3(self):
        node7 = TextNode("This is a fifth text node", "bold")
        node8 = TextNode("This is a fifth text node", "bold", "https://codybense.com")
        self.assertEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()
