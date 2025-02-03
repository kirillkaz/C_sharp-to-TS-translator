from .rules import parse_variable_declaration
from .ASTNode import ASTNode

def parse_to_AST(tokens):
    if isinstance(tokens, str):
        return tokens
    nodes = []
    position = 0

    while position < len(tokens):
        token_type, token_value = tokens[position]

        if token_type == "KEYWORD" and token_value in ["var", "new"]:
            nodes.append(parse_variable_declaration(tokens, position))
            position += 5;
        else:
            position += 1

    return ASTNode(
        type="Program",
        children=nodes
    )