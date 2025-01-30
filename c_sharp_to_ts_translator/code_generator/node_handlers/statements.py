from ..generator import handle_node

def handle_statement(node):
    """Генерация кода для операторов и блоков."""
    if node.type == "IfStatement":
        condition = handle_node(node.children[0])
        statement = handle_node(node.children[1])
        return f"if ({condition}) {{\n{statement}\n}}"
    elif node.type == "ForLoop":
        initialization = handle_node(node.children[0])
        condition = handle_node(node.children[1])
        increment = handle_node(node.children[2])
        statement = handle_node(node.children[3])
        return f"for ({initialization} {condition}; {increment}) {{\n{statement}\n}}"
    elif node.type == "SwitchStatement":
        condition = handle_node(node.children[0])
        cases = "\n".join([handle_node(case) for case in node.children[1].children])
        return f"switch ({condition}) {{\n{cases}\n}}"
    elif node.type == "Case":
        value = handle_node(node.children[0])
        statement = handle_node(node.children[1])
        return f"case {value}:\n{statement}\nbreak;"
    elif node.type == "Block":
        return "{\n" + "\n".join([handle_node(child) for child in node.children]) + "\n}"
    else:
        raise ValueError(f"Неизвестный тип оператора: {node.type}")

def handle_if_statement(node):
    """Генерация кода для оператора if."""
    condition = handle_node(node.children[0])
    statement = handle_node(node.children[1])
    return f"if ({condition}) {{ {statement} }}"

def handle_else_statement(node):
    """Генерация кода для оператора else."""
    statement = handle_node(node.children[0])
    return f"else {{ {statement} }}"

def handle_for_loop(node):
    """Генерация кода для цикла for."""
    init = handle_node(node.children[0])
    condition = handle_node(node.children[1])
    increment = handle_node(node.children[2])
    statement = handle_node(node.children[3])
    return f"for ({init}; {condition}; {increment}) {{ {statement} }}"

def handle_while_loop(node):
    """Генерация кода для цикла while."""
    condition = handle_node(node.children[0])
    statement = handle_node(node.children[1])
    return f"while ({condition}) {{ {statement} }}"

def handle_try_catch(node):
    """Генерация кода для блока try-catch."""
    try_statement = handle_node(node.children[0])
    catch_statement = handle_node(node.children[1])
    return f"try {{ {try_statement} }} catch {{ {catch_statement} }}"
