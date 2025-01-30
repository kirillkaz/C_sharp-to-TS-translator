from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier

def parse_literal(tokens, position):
    if position + 1 >= len(tokens):
        return None

    literal_token = tokens[position]
    
    if literal_token[0] == "LITERAL":
        # Проверка, что это число или строка
        return ASTNode(
            type="Literal",
            value=literal_token[1]
        )
    
    # Дополнительная проверка для возможных идентификаторов (например переменных или функций)
    identifier = parse_identifier(tokens, position)
    if identifier:
        return identifier

    return None
