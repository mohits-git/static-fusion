from enum import Enum


text_type = Enum(
    'text_type',
    ['text', 'bold', 'italic', 'code', 'link', 'image']
)
