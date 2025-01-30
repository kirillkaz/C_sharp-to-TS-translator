from ..ASTNode import ASTNode
from .expression_rule import parse_expression
from .statement_rule import parse_statement

def parse_if_statement(tokens, position):
    if position + 4 >= len(tokens):
        return None
    
    if_token, condition_token, open_brace_token, body_token = tokens[position:position + 4]
    
    # Проверяем структуру if (condition) { body }
    if if_token[0] == "KEYWORD" and if_token[1] == "if" and open_brace_token[1] == "{":
        condition_node = parse_expression(tokens, position + 1)
        body_node = []
        
        position += 1
        while position < len(tokens) and tokens[position][1] != "}":
            statement = parse_statement(tokens, position)
            if statement:
                body_node.append(statement)
                position += 1
        
        return ASTNode(
            type="IfStatement",
            children=[
                ASTNode(type="Condition", children=[condition_node]),
                ASTNode(type="Body", children=body_node)
            ]
        )
    return None
