from app.textnode import TextNode


def main():
    node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node1.__repr__())
    node2 = TextNode("Hello", "italic")
    print(node2.__repr__())
    print(node1.__eq__(node2))


main()
