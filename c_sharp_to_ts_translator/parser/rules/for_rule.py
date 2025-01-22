from ..ASTNode import ASTNode
from .expression_rule import parse_expression
from .operator_rule import parse_operator
from .statement_rule import parse_statement

def parse_for_loop(tokens, position):
    if position + 6 >= len(tokens):
        return None

    for_token, open_paren_token, init_token, condition_token, update_token, close_paren_token, open_brace_token = tokens[position:position + 7]
    
    # Ожидаем структуру: for (init; condition; update) { body }
    if for_token[0] == "KEYWORD" and for_token[1] == "for" and open_paren_token[1] == "(" and close_paren_token[1] == ")":
        init_node = parse_expression(tokens, position + 2)
        condition_node = parse_expression(tokens, position + 3)
        update_node = parse_expression(tokens, position + 4)
        
        body_node = []
        position += 5
        while position < len(tokens) and tokens[position][1] != "}":
            statement = parse_statement(tokens, position)
            if statement:
                body_node.append(statement)
                position += 1
        
        return ASTNode(
            type="ForLoop",
            children=[
                ASTNode(type="Init", children=[init_node]),
                ASTNode(type="Condition", children=[condition_node]),
                ASTNode(type="Update", children=[update_node]),
                ASTNode(type="Body", children=body_node)
            ]
        )
    return None
