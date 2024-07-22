import re
from app.block_to_block_type import block_to_block_type
from app.leafnode import LeafNode
from app.markdown_to_blocks import markdown_to_blocks
from app.parentnode import ParentNode
from app.custom_types import block_type
from app.text_to_textnodes import text_to_textnodes
from app.textnode_to_htmlnode import text_node_to_html_node


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        current_type = block_to_block_type(block)
        match(current_type):
            case block_type.heading.name:
                children.append(block_to_html_heading(block))
            case block_type.code.name:
                children.append(block_to_html_code(block))
            case block_type.quote.name:
                children.append(block_to_html_quote(block))
            case block_type.unordered_list.name:
                children.append(block_to_unordered_list(block))
            case block_type.ordered_list.name:
                children.append(block_to_ordered_list(block))
            case block_type.paragraph.name:
                children.append(block_to_html_paragraph(block))
            case _:
                raise ValueError(
                    "Invalid block_type received from block_to_block_type"
                )
    return ParentNode('div', children)


def block_to_html_heading(block):
    hashes = re.match(r"^#* ", block)
    if hashes is None:
        raise ValueError("Input block is not a Heading type block")
    num_of_hashes = hashes.span()[1] - 1
    match(num_of_hashes):
        case 1:
            return ParentNode('h1', text_to_children(block[2:]))
        case 2:
            return ParentNode('h2', text_to_children(block[3:]))
        case 3:
            return ParentNode('h3', text_to_children(block[4:]))
        case 4:
            return ParentNode('h4', text_to_children(block[5:]))
        case 5:
            return ParentNode('h5', text_to_children(block[6:]))
        case 6:
            return ParentNode('h6', text_to_children(block[7:]))
        case _:
            return ParentNode('p', text_to_children(block))


def block_to_html_code(block):
    code = block.strip('```')
    code_htmlnode = LeafNode(code, 'code')
    return ParentNode('pre', [code_htmlnode])


def block_to_html_quote(block):
    lines = block.split('\n')
    children = []
    for line in lines:
        children.append(ParentNode('p', text_to_children(line[2:])))
    return ParentNode('blockquote', children)


def block_to_unordered_list(block):
    lines = block.split('\n')
    children = []
    for line in lines:
        children.append(ParentNode('li', text_to_children(line[2:])))
    return ParentNode('ul', children)


def block_to_ordered_list(block):
    lines = block.split('\n')
    children = []
    for line in lines:
        children.append(ParentNode('li', text_to_children(line[3:])))
    return ParentNode('ol', children)


def block_to_html_paragraph(block):
    return ParentNode('p', text_to_children(block))


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes
