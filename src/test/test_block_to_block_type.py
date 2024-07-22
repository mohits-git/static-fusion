import unittest
from unittest.mock import patch
from app.custom_types import block_type
from app.block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), block_type.heading.name)

    def test_code_block(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), block_type.code.name)

    def test_quote(self):
        block = "> This is a quote\n> This is also a quote"
        self.assertEqual(block_to_block_type(block), block_type.quote.name)

    def test_unordered_list(self):
        block = "* Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(block),
                         block_type.unordered_list.name)

    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(block),
                         block_type.ordered_list.name)

    def test_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), block_type.paragraph.name)

    @patch('app.block_to_block_type.is_quote')
    def test_is_quote(self, mock_is_quote):
        block = "> Quote"
        mock_is_quote.return_value = True
        self.assertEqual(block_to_block_type(block), block_type.quote.name)
        mock_is_quote.assert_called_once_with(block)

    @patch('app.block_to_block_type.is_unordered_list')
    def test_is_unordered_list(self, mock_is_unordered_list):
        block = "* Item"
        mock_is_unordered_list.return_value = True
        self.assertEqual(block_to_block_type(block),
                         block_type.unordered_list.name)
        mock_is_unordered_list.assert_called_once_with(block)

    @patch('app.block_to_block_type.is_ordered_list')
    def test_is_ordered_list(self, mock_is_ordered_list):
        block = "1. Item"
        mock_is_ordered_list.return_value = True
        self.assertEqual(block_to_block_type(block),
                         block_type.ordered_list.name)
        mock_is_ordered_list.assert_called_once_with(block)


if __name__ == '__main__':
    unittest.main()
