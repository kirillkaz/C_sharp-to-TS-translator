from ..ASTNode import ASTNode
from .expression_rule import parse_expression

def parse_return_statement(tokens, position):
    if position + 1 >= len(tokens):
        return None
    
    return_token, expression_token = tokens[position:position + 2]

    # Ожидаем структуру: return expression;
    if return_token[0] == "KEYWORD" and return_token[1] == "return":
        expression_node = parse_expression(tokens, position + 1)

        return ASTNode(
            type="ReturnStatement",
            children=[expression_node]
        )
    return None
	