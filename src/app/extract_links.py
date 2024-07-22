import re


def extract_markdown_images(text):
    result = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return result


def extract_markdown_links(text):
    result = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return result
