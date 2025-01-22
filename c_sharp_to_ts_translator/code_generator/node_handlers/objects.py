from ..generator import handle_node

def handle_array_access(node):
    """Генерация кода для доступа к элементам массива."""
    array_name = node.children[0].value
    index = handle_node(node.children[1])
    return f"{array_name}[{index}]"

def handle_object_access(node):
    """Генерация кода для доступа к свойствам объекта."""
    object_name = node.children[0].value
    property_name = node.children[1].value
    return f"{object_name}.{property_name}"
