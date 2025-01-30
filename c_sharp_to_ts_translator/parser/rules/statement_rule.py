from ..ASTNode import ASTNode

def parse_if_statement(tokens, position):
    if position + 5 > len(tokens):
        return None, position
    
    # Ожидаем структуру: if (condition) { statement }
    if_token, condition_token, open_bracket, statement_token, close_bracket = tokens[position:position + 5]
    
    if if_token[0] == "KEYWORD" and if_token[1] == "if" and condition_token[0] == "EXPRESSION" and open_bracket[0] == "PUNCTUATION" and open_bracket[1] == "(" and close_bracket[0] == "PUNCTUATION" and close_bracket[1] == "}":
        return ASTNode(
            type="IfStatement",
            children=[
                ASTNode(type="Condition", value=condition_token[1]),
                ASTNode(type="Statement", value=statement_token[1])
            ]
        ), position + 5
    return None, position

def parse_for_loop(tokens, position):
    if position + 6 > len(tokens):
        return None, position
    
    # Ожидаем структуру: for (initialization; condition; increment) { statement }
    for_token, initialization_token, condition_token, increment_token, statement_token = tokens[position:position + 5]
    
    if for_token[0] == "KEYWORD" and for_token[1] == "for" and initialization_token[0] == "EXPRESSION" and condition_token[0] == "EXPRESSION" and increment_token[0] == "EXPRESSION":
        return ASTNode(
            type="ForLoop",
            children=[
                ASTNode(type="Initialization", value=initialization_token[1]),
                ASTNode(type="Condition", value=condition_token[1]),
                ASTNode(type="Increment", value=increment_token[1]),
                ASTNode(type="Statement", value=statement_token[1])
            ]
        ), position + 6
    return None, position

def parse_switch_statement(tokens, position):
    if position + 6 > len(tokens):
        return None, position
    
    # Ожидаем структуру: switch (expression) { case value: statement }
    switch_token, expression_token, open_bracket, case_token, value_token, statement_token = tokens[position:position + 6]
    
    if switch_token[0] == "KEYWORD" and switch_token[1] == "switch" and expression_token[0] == "EXPRESSION" and case_token[0] == "KEYWORD" and case_token[1] == "case":
        return ASTNode(
            type="SwitchStatement",
            children=[
                ASTNode(type="Expression", value=expression_token[1]),
                ASTNode(type="Case", value=value_token[1]),
                ASTNode(type="Statement", value=statement_token[1])
            ]
        ), position + 6
    return None, position

def parse_statement(tokens, position):
    parsers = [
        parse_if_statement,
        parse_for_loop,
        parse_switch_statement
    ]
    
    for parser in parsers:
        node, new_position = parser(tokens, position)
        if node is not None:
            return node, new_position
    
    return None, position
