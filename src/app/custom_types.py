from enum import Enum


text_type = Enum(
    'text_type',
    ['text', 'bold', 'italic', 'code', 'link', 'image']
)


block_type = Enum(
    'block_type',
    ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list']
)
