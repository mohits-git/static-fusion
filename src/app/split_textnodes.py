from app.extract_links import extract_markdown_images, extract_markdown_links
from app.textnode import TextNode
from app.text_type import text_type as TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text.name:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax. No closing delimiter.")
        i = 0
        while i < len(split_text):
            if len(split_text[i]) > 0:
                new_nodes.append(TextNode(split_text[i], TextType.text.name))
            if i+1 < len(split_text) and len(split_text[i+1]) > 0:
                new_nodes.append(TextNode(split_text[i+1], text_type))
            if i+2 < len(split_text) and len(split_text[i+2]) > 0:
                new_nodes.append(TextNode(split_text[i+2], TextType.text.name))
            i += 3
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text.name:
            new_nodes.append(node)
            continue
        text = node.text
        all_links = extract_markdown_links(text)
        if len(all_links) == 0:
            new_nodes.append(node)
        for link in all_links:
            split_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_text[0]) != 0:
                new_nodes.append(TextNode(split_text[0], TextType.text.name))
            new_nodes.append(TextNode(link[0], TextType.link.name, link[1]))
            text = split_text[1]
        if len(all_links) > 0 and text != '':
            new_nodes.append(TextNode(text, TextType.text.name))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text.name:
            new_nodes.append(node)
            continue
        text = node.text
        all_images = extract_markdown_images(text)
        if len(all_images) == 0:
            new_nodes.append(node)
        for image in all_images:
            split_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_text[0]) != 0:
                new_nodes.append(TextNode(split_text[0], TextType.text.name))
            new_nodes.append(TextNode(image[0], TextType.image.name, image[1]))
            text = split_text[1]
        if len(all_images) > 0 and text != '':
            new_nodes.append(TextNode(text, TextType.text.name))
    return new_nodes
