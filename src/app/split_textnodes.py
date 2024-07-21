from app.extract_links import extract_markdown_images, extract_markdown_links
from app.textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax. No closing delimiter.")
        i = 0
        while i < len(split_text):
            new_nodes.append(TextNode(split_text[i], "text"))
            if i+1 < len(split_text):
                new_nodes.append(TextNode(split_text[i+1], text_type))
            if i+2 < len(split_text):
                new_nodes.append(TextNode(split_text[i+2], "text"))
            i += 3
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "link":
            new_nodes.append(node)
            continue
        text = node.text
        all_links = extract_markdown_links(text)
        for link in all_links:
            split_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_text[0]) != 0:
                new_nodes.append(TextNode(split_text[0], 'text'))
            new_nodes.append(TextNode(link[0], 'link', link[1]))
            text = split_text[1]
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "image":
            new_nodes.append(node)
            continue
        text = node.text
        all_images = extract_markdown_images(text)
        for image in all_images:
            split_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_text[0]) != 0:
                new_nodes.append(TextNode(split_text[0], 'text'))
            new_nodes.append(TextNode(image[0], 'image', image[1]))
            text = split_text[1]
    return new_nodes
