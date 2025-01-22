from ..ASTNode import ASTNode
from .literal_rule import parse_literal
from .identifier_rule import parse_identifier

def parse_operator(tokens, position):
    if position + 1 >= len(tokens):
        return None

    operator_token = tokens[position]
    # Проверка на операторы, как например =, ==, +, -, и т.д.
    if operator_token[0] == "OPERATOR":
        operator = operator_token[1]
        
        # В случае присваивания, можно ожидать что после оператора идет выражение
        if operator == "=":
            position += 1
            expression = parse_literal(tokens, position) or parse_identifier(tokens, position)
            if expression:
                return ASTNode(
                    type="Assignment",
                    value=operator,
                    children=[expression]
                )
        return ASTNode(
            type="Operator",
            value=operator
        )
    return None
