from ..generator import handle_node

def handle_program(node):
    """Генерация кода для программы."""
    return "\n".join([handle_node(child) for child in node.children])
