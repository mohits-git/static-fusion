import unittest
from app.extract_links import extract_markdown_images, extract_markdown_links


class TestExtractLinks(unittest.TestCase):
    def test_markdown_links(self):
        text = "hello this is my [portfolio](https://www.mohits.site)"
        tuples = extract_markdown_links(text)
        expected_tuples = [
            ("portfolio", "https://www.mohits.site")
        ]
        self.assertEqual(
            tuples,
            expected_tuples,
            "TestExtractLinks:- Markdown Links Extraction Failed"
        )

    def test_markdown_images(self):
        text = "hello this is my ![picture](public/pfp/mohit.png)"
        tuples = extract_markdown_images(text)
        expected_tuples = [
            ("picture", "public/pfp/mohit.png")
        ]
        self.assertEqual(
            tuples,
            expected_tuples,
            "TestExtractLinks:- Markdown Images Extraction Failed"
        )

    def test_markdown_multiple_links(self):
        text = "hello this is my [portfolio](https://www.mohits.site) and this is my [twitter](https://www.x.com/mohits_twt)"
        tuples = extract_markdown_links(text)
        expected_tuples = [
            ("portfolio", "https://www.mohits.site"),
            ("twitter", "https://www.x.com/mohits_twt")
        ]
        self.assertEqual(
            tuples,
            expected_tuples,
            "TestExtractLinks:- Markdown Multiple Links Extraction Failed"
        )

    def test_markdown_multiple_images(self):
        text = "hello this is my ![picture](public/pfp/mohit.png) ![my dog's picture](public/pfp/dog.png)"
        tuples = extract_markdown_images(text)
        expected_tuples = [
            ("picture", "public/pfp/mohit.png"),
            ("my dog's picture", "public/pfp/dog.png")
        ]
        self.assertEqual(
            tuples,
            expected_tuples,
            "TestExtractLinks:- Markdown Multiple Images Extraction Failed"
        )

    def test_markdown_mixed_images(self):
        text = "hello this is my ![picture](public/pfp/mohit.png) [my dog's picture](public/pfp/dog.png)"
        tuples = extract_markdown_images(text)
        expected_tuples = [
            ("picture", "public/pfp/mohit.png"),
        ]
        self.assertEqual(
            tuples,
            expected_tuples,
            "TestExtractLinks:- Markdown Mixed Images Extraction Failed"
        )

    def test_markdown_mixed_links(self):
        text = "hello this is my ![picture](public/pfp/mohit.png) [my dog's picture](public/pfp/dog.png)"
        tuples = extract_markdown_links(text)
        expected_tuples = [
            ("my dog's picture", "public/pfp/dog.png")
        ]
        self.assertEqual(
            tuples,
            expected_tuples,
            "TestExtractLinks:- Markdown Mixed Links Extraction Failed"
        )
