from ..ASTNode import ASTNode
from .expression_rule import parse_expression

def parse_array_access(tokens, position):
    if position + 2 >= len(tokens):
        return None

    array_token, open_bracket_token, index_token, close_bracket_token = tokens[position:position + 4]

    # Ожидаем структуру: array[index]
    if array_token[0] == "IDENTIFIER" and open_bracket_token[1] == "[" and close_bracket_token[1] == "]":
        index_node = parse_expression(tokens, position + 2)

        return ASTNode(
            type="ArrayAccess",
            children=[
                ASTNode(type="Array", value=array_token[1]),
                ASTNode(type="Index", children=[index_node])
            ]
        )
    return None
