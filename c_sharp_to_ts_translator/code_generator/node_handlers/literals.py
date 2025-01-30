def handle_literal(node):
    """Генерация кода для литералов."""
    if node.type == "Number":
        return str(node.value)
    elif node.type == "String":
        return f'"{node.value}"'
    elif node.type == "Boolean":
        return "true" if node.value else "false"
    else:
        raise ValueError(f"Неизвестный тип литерала: {node.type}")
