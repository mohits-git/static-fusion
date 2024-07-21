import unittest
from app.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("This is the text inside the leaf node", "p")
        expected_str = '<p>This is the text inside the leaf node</p>'
        self.assertEqual(node1.to_html(), expected_str, "LeafNode test failed")

    def test_to_html_plaintext(self):
        node2 = LeafNode("Holla this is the plain text")
        expected_str = 'Holla this is the plain text'
        self.assertEqual(node2.to_html(), expected_str, "LeafNode test failed")


if __name__ == "__main__":
    unittest.main()
