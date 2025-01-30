from ..ASTNode import ASTNode
from .statement_rule import parse_statement

def parse_else_statement(tokens, position):
    if position + 2 >= len(tokens):
        return None
    
    else_token, open_brace_token, body_token = tokens[position:position + 3]
    
    # Ожидаем структуру else { body }
    if else_token[0] == "KEYWORD" and else_token[1] == "else" and open_brace_token[1] == "{":
        body_node = []
        
        position += 1
        while position < len(tokens) and tokens[position][1] != "}":
            statement = parse_statement(tokens, position)
            if statement:
                body_node.append(statement)
                position += 1
        
        return ASTNode(
            type="ElseStatement",
            children=[ASTNode(type="Body", children=body_node)]
        )
    return None
