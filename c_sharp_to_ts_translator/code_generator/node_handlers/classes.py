from ..generator import handle_node

def handle_class_declaration(node):
    """Генерация кода для объявления класса."""
    class_name = node.children[0].value
    body = "\n".join([handle_node(child) for child in node.children[1].children])
    return f"class {class_name} {{\n{body}\n}}"

def handle_function_declaration(node):
    """Генерация кода для объявления функции."""
    return_type = node.children[0].value  # Тип возвращаемого значения
    func_name = node.children[1].value  # Имя функции
    params = ", ".join([handle_node(param) for param in node.children[2].children])
    body = "\n".join([handle_node(child) for child in node.children[3].children])
    return f"{return_type} {func_name}({params}) {{\n{body}\n}}"

def handle_namespace(node):
    """Генерация кода для пространства имён."""
    namespace_name = node.children[0].value
    body = "\n".join([handle_node(child) for child in node.children[1].children])
    return f"namespace {namespace_name} {{\n{body}\n}}"
