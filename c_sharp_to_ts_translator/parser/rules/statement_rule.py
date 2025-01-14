from ..ASTNode import ASTNode

# TODO: position
def parse_if_statement(tokens):
    if len(tokens) < 4:
        return None
    
    # Ожидаем структуру: if (condition) { statement }
    if_token, condition_token, open_bracket, statement_token, close_bracket = tokens[:5]
    
    if if_token[0] == "KEYWORD" and condition_token[0] == "EXPRESSION" and open_bracket[0] == "PUNCTUATION" and close_bracket[0] == "PUNCTUATION":
        return ASTNode(
            type="IfStatement",
            children=[
                ASTNode(type="Condition", value=condition_token[1]),
                ASTNode(type="Statement", value=statement_token[1])
            ]
        )
    return None

# TODO: position
def parse_for_loop(tokens):
    if len(tokens) < 6:
        return None
    
    # Ожидаем структуру: for (initialization; condition; increment) { statement }
    for_token, initialization_token, condition_token, increment_token, statement_token = tokens[:5]
    
    if for_token[0] == "KEYWORD" and initialization_token[0] == "EXPRESSION" and condition_token[0] == "EXPRESSION" and increment_token[0] == "EXPRESSION":
        return ASTNode(
            type="ForLoop",
            children=[
                ASTNode(type="Initialization", value=initialization_token[1]),
                ASTNode(type="Condition", value=condition_token[1]),
                ASTNode(type="Increment", value=increment_token[1]),
                ASTNode(type="Statement", value=statement_token[1])
            ]
        )
    return None

def parse_switch_statement(tokens):
    if len(tokens) < 4:
        return None
    
    # Ожидаем структуру: switch (expression) { case value: statement }
    switch_token, expression_token, open_bracket, case_token, value_token, statement_token = tokens[:6]
    
    if switch_token[0] == "KEYWORD" and expression_token[0] == "EXPRESSION" and case_token[0] == "KEYWORD":
        return ASTNode(
            type="SwitchStatement",
            children=[
                ASTNode(type="Expression", value=expression_token[1]),
                ASTNode(type="Case", value=value_token[1]),
                ASTNode(type="Statement", value=statement_token[1])
            ]
        )
    return None
