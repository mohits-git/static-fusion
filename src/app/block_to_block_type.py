import re
from app.custom_types import block_type


def block_to_block_type(block):
    if re.match(r"^#* ", block) is not None:
        return block_type.heading.name
    elif block.startswith('```') and block.endswith('```'):
        return block_type.code.name
    elif is_quote(block):
        return block_type.quote.name
    elif is_unordered_list(block):
        return block_type.unordered_list.name
    elif is_ordered_list(block):
        return block_type.ordered_list.name
    else:
        return block_type.paragraph.name


def is_quote(block):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith('>'):
            return False
    return True


def is_unordered_list(block):
    lines = block.split('\n')
    for line in lines:
        if re.match(r"^[\*-] ", line) is None:
            return False
    return True


def is_ordered_list(block):
    lines = block.split('\n')
    for line in lines:
        if re.match(r"^\d{1}. ", line) is None:
            return False
    return True
