from app.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        html_node_str = ""
        if self.tag is not None:
            html_node_str += f"<{self.tag}"
        html_node_str += self.props_to_html()
        html_node_str += ">"
        html_node_str += str(self.value)
        if self.tag is not None:
            html_node_str += f"<{'/'}{self.tag}>"
        return html_node_str
