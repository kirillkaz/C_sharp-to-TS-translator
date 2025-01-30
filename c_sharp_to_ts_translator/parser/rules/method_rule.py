from ..ASTNode import ASTNode
from .declaration_rule import parse_variable_declaration
from .operator_rule import parse_operator
from .literal_rule import parse_literal
from .identifier_rule import parse_identifier
from .delimiter_rule import parse_delimiter

def parse_method_call(tokens, position):
    if position + 1 >= len(tokens):
        return None

    method_token, open_paren_token, *rest = tokens[position:]
    
    if method_token[0] != "STANDART_METHODS" or open_paren_token[0] != "DELIMITER" or open_paren_token[1] != "(":
        return None

    method_name = method_token[1]
    parameters = parse_parameters(tokens, position + 2)

    if parameters is None or rest[0][0] != "DELIMITER" or rest[0][1] != ")":
        return None

    return ASTNode(
        type="MethodDeclaration",
        children=[
            ASTNode(type="MethodName", value=method_name),
            parameters
        ]
    )

def parse_parameters(tokens, position):
    params = []
    while position < len(tokens) and tokens[position][0] != "DELIMITER" and tokens[position][1] != ")":
        param = parse_variable_declaration(tokens, position)
        if param:
            params.append(param)
            position += 1
        else:
            param = parse_operator(tokens, position)
            if param:
                params.append(param)
                position += 1
            else:
                break
    return ASTNode(type="Parameters", children=params)
