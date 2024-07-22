import unittest
from app.split_textnodes import split_nodes_delimiter
from app.textnode import TextNode
from app.types import text_type


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [
            TextNode('holla this is **bold** text', text_type.text.name),
            TextNode('This is mofkin **BOLD** text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", text_type.bold.name)
        expected_nodes = [
            TextNode('holla this is ', text_type.text.name),
            TextNode('bold', text_type.bold.name),
            TextNode(' text', text_type.text.name),
            TextNode('This is mofkin ', text_type.text.name),
            TextNode('BOLD', text_type.bold.name),
            TextNode(' text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Delimiter Test failed")

    def test_italic(self):
        old_nodes = [
            TextNode('holla this is *italic* text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
            TextNode('This is mofkin *italic* text', text_type.text.name),
            TextNode('*italic text it is*', text_type.italic.name),
        ]
        new_nodes = split_nodes_delimiter(
            old_nodes, "*", text_type.italic.name)
        expected_nodes = [
            TextNode('holla this is ', text_type.text.name),
            TextNode('italic', text_type.italic.name),
            TextNode(' text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
            TextNode('This is mofkin ', text_type.text.name),
            TextNode('italic', text_type.italic.name),
            TextNode(' text', text_type.text.name),
            TextNode('*italic text it is*', text_type.italic.name),
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Delimiter Test failed")

    def test_code(self):
        old_nodes = [
            TextNode('holla this is `code` text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
            TextNode('This is mofkin `code` text', text_type.text.name),
            TextNode('`code text it is`', text_type.code.name),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", text_type.code.name)
        expected_nodes = [
            TextNode('holla this is ', text_type.text.name),
            TextNode('code', text_type.code.name),
            TextNode(' text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
            TextNode('This is mofkin ', text_type.text.name),
            TextNode('code', text_type.code.name),
            TextNode(' text', text_type.text.name),
            TextNode('`code text it is`', text_type.code.name),
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Delimiter Test failed")

    def test_invalid_markdown(self):
        old_nodes = [
            TextNode('holla this is `code` text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
            TextNode('This is mofkin `code text', text_type.text.name),
            TextNode('`code text it is`', text_type.code.name),
        ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "`", text_type.code.name)

    def test_markdown_with_only_texttype_bold(self):
        old_nodes = [
            TextNode('**bold text it is**', text_type.text.name),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", text_type.bold.name)
        expected_nodes = [
            TextNode('bold text it is', text_type.bold.name),
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Delimiter Test failed")

    def test_multiple_splits(self):
        old_nodes = [
            TextNode('holla this is **bold** and **another bold** text',
                     text_type.text.name),
            TextNode('This is mofkin **BOLD** text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", text_type.bold.name)
        expected_nodes = [
            TextNode('holla this is ', text_type.text.name),
            TextNode('bold', text_type.bold.name),
            TextNode(' and ', text_type.text.name),
            TextNode('another bold', text_type.bold.name),
            TextNode(' text', text_type.text.name),
            TextNode('This is mofkin ', text_type.text.name),
            TextNode('BOLD', text_type.bold.name),
            TextNode(' text', text_type.text.name),
            TextNode('**bold text it is**', text_type.bold.name),
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Delimiter Test failed")
