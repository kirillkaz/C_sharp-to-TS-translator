from ..ASTNode import ASTNode
from .expression_rule import parse_expression
from .statement_rule import parse_statement

def parse_case_statement(tokens, position):
    if position + 2 >= len(tokens):
        return None
    
    case_token, condition_token, colon_token = tokens[position:position + 3]

    # Ожидаем структуру: case condition: body
    if case_token[0] == "KEYWORD" and case_token[1] == "case" and colon_token[1] == ":":
        condition_node = parse_expression(tokens, position + 1)
        body_node = []
        
        position += 2
        while position < len(tokens) and tokens[position][1] != "case" and tokens[position][1] != "}":
            statement = parse_statement(tokens, position)
            if statement:
                body_node.append(statement)
                position += 1

        return ASTNode(
            type="CaseStatement",
            children=[
                ASTNode(type="Condition", children=[condition_node]),
                ASTNode(type="Body", children=body_node)
            ]
        )
    return None
