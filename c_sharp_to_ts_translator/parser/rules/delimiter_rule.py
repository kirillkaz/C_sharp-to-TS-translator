from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier
from .operator_rule import parse_operator

def parse_delimiter(tokens, position):
    if position + 1 >= len(tokens):
        return None

    delimiter_token = tokens[position]

    if delimiter_token[0] == "DELIMITER":
        value = delimiter_token[1]
        
        # Разделитель как точка с запятой, скобка, фигурная скобка и т.д.
        return ASTNode(
            type="Delimiter",
            value=value
        )
    return None
