from ..ASTNode import ASTNode
from .literal_rule import parse_literal

def parse_string(tokens, position):
    if position + 1 >= len(tokens):
        return None

    string_token = tokens[position]
    
    if string_token[0] == "STRING":
        return ASTNode(
            type="StringLiteral",
            value=string_token[1][1:-1]  # Убираем кавычки из строки
        )
    return None
