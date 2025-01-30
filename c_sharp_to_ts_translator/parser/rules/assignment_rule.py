from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier
from .expression_rule import parse_expression
from .operator_rule import parse_operator

def parse_assignment(tokens, position):
    if position + 3 >= len(tokens):
        return None
    
    identifier_token, assignment_token, expression_token = tokens[position:position + 3]

    # Ожидаем структуру: identifier = expression;
    if identifier_token[0] == "IDENTIFIER" and assignment_token[0] == "OPERATOR" and assignment_token[1] == "=":
        identifier_node = parse_identifier(tokens, position)
        expression_node = parse_expression(tokens, position + 2)

        return ASTNode(
            type="Assignment",
            children=[
                ASTNode(type="Identifier", children=[identifier_node]),
                ASTNode(type="Expression", children=[expression_node])
            ]
        )
    return None
