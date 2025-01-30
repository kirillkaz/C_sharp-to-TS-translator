from ..ASTNode import ASTNode

def parse_variable_declaration(tokens, position):
    if position + 4 >= len(tokens):
        return None
    
    # Ожидаем структуру: type identifier = value ;
    type_token, identifier_token, assignment_token, value_token, semicolon_token = tokens[position:position + 5]
    
    if type_token[0] == "KEYWORD" and assignment_token[0] == "OPERATOR" and assignment_token[1] == "=" and semicolon_token[0] == "DELIMITER" and semicolon_token[1] == ";":
        return ASTNode(	
            type="VariableDeclaration",
            children=[
                ASTNode(type="Type", value=type_token[1]),
                ASTNode(type="Identifier", value=identifier_token[1]),
                ASTNode(type="Value", value=parse_value(value_token))
            ]
        )
    return None

def parse_value(token):
    if token[0] == "NUMBER":
        return int(token[1])
    elif token[0] == "STRING":
        return token[1][1:-1]
    return None
