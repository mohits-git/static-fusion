import unittest
from app.split_textnodes import split_nodes_delimiter
from app.textnode import TextNode


text_type_text = "text"
text_type_code = "code"
text_type_bold = "bold"
text_type_italic = "italic"


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [
            TextNode('holla this is **bold** text', text_type_text),
            TextNode('This is mofkin **BOLD** text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", text_type_bold)
        expected_nodes = [
            TextNode('holla this is ', text_type_text),
            TextNode('bold', text_type_bold),
            TextNode(' text', text_type_text),
            TextNode('This is mofkin ', text_type_text),
            TextNode('BOLD', text_type_bold),
            TextNode(' text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic(self):
        old_nodes = [
            TextNode('holla this is *italic* text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
            TextNode('This is mofkin *italic* text', text_type_text),
            TextNode('*italic text it is*', text_type_italic),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "*", text_type_italic)
        expected_nodes = [
            TextNode('holla this is ', text_type_text),
            TextNode('italic', text_type_italic),
            TextNode(' text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
            TextNode('This is mofkin ', text_type_text),
            TextNode('italic', text_type_italic),
            TextNode(' text', text_type_text),
            TextNode('*italic text it is*', text_type_italic),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_code(self):
        old_nodes = [
            TextNode('holla this is `code` text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
            TextNode('This is mofkin `code` text', text_type_text),
            TextNode('`code text it is`', text_type_code),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", text_type_code)
        expected_nodes = [
            TextNode('holla this is ', text_type_text),
            TextNode('code', text_type_code),
            TextNode(' text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
            TextNode('This is mofkin ', text_type_text),
            TextNode('code', text_type_code),
            TextNode(' text', text_type_text),
            TextNode('`code text it is`', text_type_code),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_invalid_markdown(self):
        old_nodes = [
            TextNode('holla this is `code` text', text_type_text),
            TextNode('**bold text it is**', text_type_bold),
            TextNode('This is mofkin `code text', text_type_text),
            TextNode('`code text it is`', text_type_code),
        ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "`", text_type_code)
