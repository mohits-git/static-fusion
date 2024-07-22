import unittest

from app.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title_extraction(self):
        markdown = "# This is a title\nSome content here."
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_title_with_special_characters(self):
        markdown = "# With $pecial Ch@racters!"
        self.assertEqual(extract_title(markdown), "With $pecial Ch@racters!")

    def test_title_not_at_beginning(self):
        markdown = "Some content\n# This is the title\nMore content"
        self.assertEqual(extract_title(markdown), "This is the title")

    def test_multiple_titles(self):
        markdown = "# First title\n## Second title\n# Third title"
        self.assertEqual(extract_title(markdown), "First title")

    def test_empty_title(self):
        markdown = "#"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_no_title_present(self):
        markdown = "This is just some text\nwithout a title"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_empty_input(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_title_with_spaces(self):
        markdown = "#    Title with spaces   "
        self.assertEqual(extract_title(markdown), "Title with spaces")

    def test_ignore_lower_level_titles(self):
        markdown = "### This is not a top-level title\n# This is the correct title"
        self.assertEqual(extract_title(markdown), "This is the correct title")

    def test_unicode_title(self):
        markdown = "# 这是一个中文标题"
        self.assertEqual(extract_title(markdown), "这是一个中文标题")


if __name__ == '__main__':
    unittest.main()
