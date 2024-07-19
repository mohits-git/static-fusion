import unittest
from app.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("This is the text inside the leaf node", "p")
        print('-------------TEST LeafNode - to_html() ---------------')
        print(node1.to_html())
        print('------------------------------------------------------')

    def test_to_html_plaintext(self):
        node2 = LeafNode("Holla this is the plain text")
        print('-------------TEST LeafNode - to_html() [for plain text] ---------------')
        print(node2.to_html())
        print('------------------------------------------------------')


if __name__ == "__main__":
    unittest.main()
