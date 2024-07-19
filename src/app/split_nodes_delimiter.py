from app.textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax. No closing delimiter found.")
        i = 0
        while i < len(split_text):
            new_nodes.append(TextNode(split_text[i], "text"))
            if i+1 < len(split_text):
                new_nodes.append(TextNode(split_text[i+1], text_type))
            if i+2 < len(split_text):
                new_nodes.append(TextNode(split_text[i+2], "text"))
            i += 3
    return new_nodes
