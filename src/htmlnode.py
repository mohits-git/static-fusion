class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, node):
        if (
            self.tag == node.tag
            and self.value == node.value
            and self.children == node.children
            and self.props == node.props
        ):
            return True
        return False

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props = self.props
        html_props = ""
        for key, value in props.items():
            html_props = f'{html_props} {key}="{value}"'
        return html_props

    def __repr__(self):
        html_node_str = ""
        if self.tag is not None:
            html_node_str += f"<{self.tag}"
        html_node_str += self.props_to_html()
        html_node_str += ">"
        if self.value is not None:
            html_node_str += self.value
        if self.children is not None:
            for child in self.children:
                html_node_str += f'\n{child.__repr__()}\n'
        if self.tag is not None:
            html_node_str += f"<{'/'}{self.tag}>"
        return html_node_str
