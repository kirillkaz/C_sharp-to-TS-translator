from ..ASTNode import ASTNode
from .statement_rule import parse_statement
from .expression_rule import parse_expression

def parse_try_catch(tokens, position):
    if position + 6 >= len(tokens):
        return None
    
    try_token, open_brace_token, body_token, catch_token, open_paren_token, error_token, close_paren_token = tokens[position:position + 7]
    
    # Ожидаем структуру: try { body } catch (error) { errorHandling }
    if try_token[0] == "KEYWORD" and try_token[1] == "try" and open_brace_token[1] == "{":
        body_node = []
        
        position += 1
        while position < len(tokens) and tokens[position][1] != "}":
            statement = parse_statement(tokens, position)
            if statement:
                body_node.append(statement)
                position += 1
        
        # Обработка catch блока
        if catch_token[0] == "KEYWORD" and catch_token[1] == "catch" and open_paren_token[1] == "(" and close_paren_token[1] == ")":
            error_node = parse_expression(tokens, position + 4)
            error_handling_node = []
            position += 5
            while position < len(tokens) and tokens[position][1] != "}":
                statement = parse_statement(tokens, position)
                if statement:
                    error_handling_node.append(statement)
                    position += 1
            return ASTNode(
                type="TryCatch",
                children=[
                    ASTNode(type="TryBody", children=body_node),
                    ASTNode(type="CatchBody", children=[ASTNode(type="Error", children=[error_node])] + error_handling_node)
                ]
            )
    return None
