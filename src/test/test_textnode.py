import unittest

from app.textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node3 = TextNode("This is another node", "bold")
        node4 = TextNode("Hello ", "bold")
        self.assertNotEqual(node3, node4)

    def test_urlnone(self):
        node5 = TextNode("This is another node", "bold", "https://google.com")
        node6 = TextNode("This is another node", "bold")
        self.assertNotEqual(node5, node6)

    def test_eqwithurl(self):
        node3 = TextNode("This is another node", "bold", "https://google.com")
        node4 = TextNode("Hello ", "bold", "https://google.com")
        self.assertNotEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()
