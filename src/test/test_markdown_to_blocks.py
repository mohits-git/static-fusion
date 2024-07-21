import unittest
from app.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = f"# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            expected_blocks,
            "Markdown to Blocks conversion test failed"
        )

    def test_markdown_with_empty_blocks(self):
        markdown = f"# This is a heading\n\n     \n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            expected_blocks,
            "Markdown to Blocks conversion test failed"
        )

    def test_markdown_with_trailing_spaces(self):
        markdown = f"# This is a heading\n\n     \n\n              \n\n         This is a paragraph of text. It has some **bold** and *italic* words inside of it.           \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item           "
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            expected_blocks,
            "Markdown to Blocks conversion test failed"
        )

    def test_markdown_with_empty_blocks_and_spaces(self):
        markdown = f"# This is a heading\n             \nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            expected_blocks,
            "Markdown to Blocks conversion test failed"
        )
