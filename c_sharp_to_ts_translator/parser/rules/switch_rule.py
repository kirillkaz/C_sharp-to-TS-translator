from ..ASTNode import ASTNode
from .expression_rule import parse_expression
from .case_rule import parse_case_statement

def parse_switch_statement(tokens, position):
    if position + 4 >= len(tokens):
        return None, position

    switch_token, open_paren_token, condition_token, close_paren_token, open_brace_token = tokens[position:position + 5]

    # Ожидаем структуру: switch (condition) { case ... }
    if switch_token[0] == "KEYWORD" and switch_token[1] == "switch" and open_paren_token[1] == "(" and close_paren_token[1] == ")":
        condition_node = parse_expression(tokens, position + 2)
        
        case_nodes = []
        position += 5
        while position < len(tokens) and tokens[position][1] != "}":
            case_node = parse_case_statement(tokens, position)
            if case_node:
                case_nodes.append(case_node)
            position += 1

        return ASTNode(
            type="SwitchStatement",
            children=[
                ASTNode(type="Condition", children=[condition_node]),
                ASTNode(type="Cases", children=case_nodes),
            ]
        ), position + 1
    return None, position
