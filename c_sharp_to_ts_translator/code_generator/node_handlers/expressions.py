from ..generator import handle_node

def handle_expression(node):
    """Генерация кода для выражений."""
    if node.type == "BinaryExpression":
        left = handle_node(node.children[0])
        operator = node.children[1].value
        right = handle_node(node.children[2])
        return f"({left} {operator} {right})"
    elif node.type == "UnaryExpression":
        operator = node.children[0].value
        operand = handle_node(node.children[1])
        return f"{operator}{operand}"
    elif node.type == "AssignmentExpression":
        variable = node.children[0].value
        value = handle_node(node.children[1])
        return f"{variable} = {value};"
    else:
        raise ValueError(f"Неизвестный тип выражения: {node.type}")

def handle_variable_declaration(node):
    """Генерация кода для декларации переменной."""
    var_type = node.children[0].value  # Тип переменной
    var_name = node.children[1].value  # Имя переменной
    value = handle_node(node.children[2]) if len(node.children) > 2 else ""
    return f"{var_type} {var_name} = {value};"

def handle_assignment_expression(node):
    """Генерация кода для присваивания."""
    variable = node.children[0].value
    value = handle_node(node.children[1])
    return f"{variable} = {value};"