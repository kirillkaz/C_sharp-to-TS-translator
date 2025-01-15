from ..ASTNode import ASTNode

def parse_binary_expression(tokens, position):
    left_token, operator_token, right_token = tokens[position:position + 3]

    if operator_token[0] == "OPERATOR" and \
       (left_token[0] in ["NUMBER", "IDENTIFIER"]) and \
       (right_token[0] in ["NUMBER", "IDENTIFIER"]):
        ast_node = ASTNode(
            type="BinaryExpression",
            children=[
                ASTNode(type="LeftOperand", value=left_token[1]),
                ASTNode(type="Operator", value=operator_token[1]),
                ASTNode(type="RightOperand", value=right_token[1])
            ]
        )
        position += 3
        return ast_node, position
    
    return None, position

def parse_unary_expression(tokens, position):
    if position + 1 >= len(tokens):
        return None, position

    operator_token, operand_token = tokens[position:position + 2]

    if operator_token[0] == "OPERATOR" and operand_token[0] == "NUMBER":
        ast_node = ASTNode(
            type="UnaryExpression",
            children=[
                ASTNode(type="Operator", value=operator_token[1]),
                ASTNode(type="Operand", value=operand_token[1])
            ]
        )
        return ast_node, position + 2
    
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
