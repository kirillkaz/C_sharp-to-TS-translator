from ..ASTNode import ASTNode
from .expression_rule import parse_expression

def parse_object_access(tokens, position):
    if position + 2 >= len(tokens):
        return None

    object_token, dot_token, property_token = tokens[position:position + 3]

    # Ожидаем структуру: object.property
    if object_token[0] == "IDENTIFIER" and dot_token[1] == ".":
        property_node = parse_expression(tokens, position + 2)

        return ASTNode(
            type="ObjectAccess",
            children=[
                ASTNode(type="Object", value=object_token[1]),
                ASTNode(type="Property", value=property_token[1])
            ]
        )
    return None
