from ..ASTNode import ASTNode

def parse_identifier(tokens, position):
    if position + 1 >= len(tokens):
        return None

    identifier_token = tokens[position]
    
    if identifier_token[0] == "IDENTIFIER":
        return ASTNode(
            type="Identifier",
            value=identifier_token[1]
        )
    return None
