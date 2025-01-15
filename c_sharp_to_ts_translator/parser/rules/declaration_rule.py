from ..ASTNode import ASTNode
from .expression_rule import parse_binary_expression, parse_unary_expression

def parse_variable_declaration(tokens, position):
    type_token, identifier_token, assignment_token, semicolon_token = tokens[position:position + 4]

    # Добавляем проверку для различных типов данных
    if type_token[1] in {"int", "double", "float", "bool", "string", "char"} and assignment_token[1] == "=":
        expression, new_position = parse_expression(type_token[1], tokens, position + 3)

        if expression:
            node = ASTNode(
                type="VariableDeclaration",
                children=[
                    ASTNode(type="Type", value=type_token[1]),
                    ASTNode(type="Identifier", value=identifier_token[1]),
                    ASTNode(type="Value", children=[expression])
                ]
            )
            return node, new_position + 1
    return None, position

def parse_expression(data_type, tokens, position):
    # Проверяем, есть ли токены для обработки
    if position >= len(tokens):
        return None, position

    # Попытка разобрать литерал (одиночный токен)
    node = parse_literal(data_type, tokens[position])
    if node:
        return node, position + 1

    # Попытка разобрать бинарное выражение
    if position + 2 < len(tokens) and tokens[position + 1][0] == "OPERATOR":
        node, new_position = parse_binary_expression(tokens, position)
        if node:
            return node, new_position

    # Попытка разобрать унарное выражение
    if position + 1 < len(tokens):
        node, new_position = parse_unary_expression(tokens, position)
        if node:
            return node, new_position

    # Если ни одно правило не сработало
    return None, position


def parse_literal(data_type, token):
    if token[0] != "LITERAL":
        return None
    if data_type == "int":
        return ASTNode(type="Literal", value=int(token[1]))
    elif data_type == "double":
        return ASTNode(type="Literal", value=float(token[1]))
    elif data_type == "float":
        return ASTNode(type="Literal", value=float(token[1]))
    elif data_type == "bool":
        return ASTNode(type="Literal", value=token[1].lower() == "true")
    elif data_type == "string":
        return ASTNode(type="Literal", value=token[1][1:-1])  # Убираем кавычки вокруг строки
    elif data_type == "char":
        return ASTNode(type="Literal", value=token[1][1])  # Убираем одинарные кавычки
    return ASTNode(type="Literal", value=token[1])
