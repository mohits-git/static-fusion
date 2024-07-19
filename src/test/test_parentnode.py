import unittest
from app.parentnode import ParentNode
from app.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent(self):
        node1 = ParentNode("div", [
            LeafNode("This is para", "p", {"class": "test-sm"}),
            LeafNode("This is anchor", "a", {"class": "test-sm"}),
            LeafNode("This is just text", None, {"class": "text-lg"})
        ], {
            "class": "flex items-center, justify-center"
        })
        print("----------------TEST PARENT NODE--------------")
        print(node1.to_html())
        print("----------------------------------------------")

    def test_parent_with_parent(self):
        node1 = ParentNode("div", [
            LeafNode("This is para", "p", {"class": "test-sm"}),
            LeafNode("This is anchor", "a", {"class": "test-sm"}),
            LeafNode("This is just text", None, {"class": "text-lg"})
        ], {
            "class": "flex items-center, justify-center"
        })
        node2 = ParentNode("span", [
            LeafNode("This is anchor", "a", {"class": "test-sm"}),
        ], {
            "class": "flex items-center, justify-center"
        })
        node3 = ParentNode("div", [
            node1,
            node2
        ])
        print("----------------TEST PARENT NODE--------------")
        print(node3.to_html())
        print("---------------------------------------------")

    def test_parent_no_tag(self):
        node1 = ParentNode(None, [], None)
        with self.assertRaises(ValueError):
            node1.to_html()

    def test_parent_no_children(self):
        node1 = ParentNode(None, [], None)
        with self.assertRaises(ValueError):
            node1.to_html()


if __name__ == "__main___":
    unittest.main()
