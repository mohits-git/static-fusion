from enum import Enum


text_type = Enum(
    'text_type',
    ['text', 'bold', 'italic', 'code', 'link', 'image']
)


# print(text_type.text.value) # 1
# print(text_type.bold.name) # bold
