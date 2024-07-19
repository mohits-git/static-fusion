from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("html tag is required")
        html_node_str = ""
        html_node_str += f"<{self.tag}"
        html_node_str += self.props_to_html()
        html_node_str += ">"
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent HTMl tag children are need.")
        for child in self.children:
            html_node_str += f'\n{child.to_html()}\n'
        if self.tag is not None:
            html_node_str += f"<{'/'}{self.tag}>"
        return html_node_str
