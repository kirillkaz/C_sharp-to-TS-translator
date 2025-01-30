from ..generator import handle_node


def handle_method_call(node):
    """Генерация кода для вызова метода."""
    method_name = node.children[0].value
    args = ", ".join([handle_node(arg) for arg in node.children[1].children])
    return f"{method_name}({args})"
