import re


def markdown_to_blocks(text):
    blocks = re.split(r"\n\s*\n", text)
    trimmed_filtered_blocks = []
    for block in blocks:
        trimmed_block = block.strip()
        if len(trimmed_block) != 0:
            trimmed_filtered_blocks.append(trimmed_block)
    return trimmed_filtered_blocks
