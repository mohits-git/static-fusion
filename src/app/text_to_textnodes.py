from app.textnode import TextNode
from app.types import text_type
from app.split_textnodes import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link
)


def text_to_textnodes(text):
    initial_textnodes = [TextNode(text, text_type.text.name)]
    split_bold_nodes = split_nodes_delimiter(
        initial_textnodes,
        '**',
        text_type.bold.name
    )
    split_italic_nodes = split_nodes_delimiter(
        split_bold_nodes,
        '*',
        text_type.italic.name
    )
    split_code_nodes = split_nodes_delimiter(
        split_italic_nodes,
        '`',
        text_type.code.name
    )
    split_link_nodes = split_nodes_link(split_code_nodes)
    split_image_nodes = split_nodes_image(split_link_nodes)
    return split_image_nodes
