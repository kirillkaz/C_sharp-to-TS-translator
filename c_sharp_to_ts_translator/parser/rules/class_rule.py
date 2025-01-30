from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier
from .function_rule import parse_function_declaration
from .declaration_rule import parse_variable_declaration

def parse_class_declaration(tokens, position):
    if position + 3 >= len(tokens):
        return None

    class_token, identifier_token, delimiter_token, body_token = tokens[position:position + 4]

    # Ожидаем структуру: class MyClass { ... }
    if class_token[0] == "KEYWORD" and class_token[1] == "class" and delimiter_token[1] == "{":
        class_node = ASTNode(
            type="Class",
            value=identifier_token[1],
            children=[]
        )
        
        # Добавление методов и переменных внутри класса
        position += 1
        while position < len(tokens):
            # Разбираем переменные и методы внутри класса
            variable_declaration = parse_variable_declaration(tokens, position)
            if variable_declaration:
                class_node.children.append(variable_declaration)
                position += 1
            method_declaration = parse_function_declaration(tokens, position)
            if method_declaration:
                class_node.children.append(method_declaration)
                position += 1
            if tokens[position][1] == "}":
                break
            position += 1
        return class_node
    return None
