class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        return f"ASTNode(type={self.type}, value={self.value}, children={self.children})"
