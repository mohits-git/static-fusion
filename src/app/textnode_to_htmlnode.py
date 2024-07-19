from app.leafnode import LeafNode


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case "text":
            return LeafNode(text_node.text)
        case "bold":
            return LeafNode(text_node.text, "b")
        case "italic":
            return LeafNode(text_node.text, "i")
        case "code":
            return LeafNode(text_node.text, "code")
        case "link":
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        case "image":
            return LeafNode(None, "img", {
                "src": text_node.url,
                "alt": "image"
            })
        case _:
            raise ValueError("Invalid TextNode Type")
