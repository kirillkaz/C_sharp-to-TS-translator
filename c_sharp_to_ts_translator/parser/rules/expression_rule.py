from ..ASTNode import ASTNode

def parse_binary_expression(tokens):
    if len(tokens) < 3:
        return None
    
    left_token, operator_token, right_token = tokens[:3]
    
    if operator_token[0] == "OPERATOR" and left_token[0] == "NUMBER" and right_token[0] == "NUMBER":
        return ASTNode(
            type="BinaryExpression",
            children=[
                ASTNode(type="LeftOperand", value=left_token[1]),
                ASTNode(type="Operator", value=operator_token[1]),
                ASTNode(type="RightOperand", value=right_token[1])
            ]
        )
    return None

def parse_unary_expression(tokens):
    if len(tokens) < 2:
        return None
    
    operator_token, operand_token = tokens[:2]
    
    if operator_token[0] == "OPERATOR" and operand_token[0] == "NUMBER":
        return ASTNode(
            type="UnaryExpression",
            children=[
                ASTNode(type="Operator", value=operator_token[1]),
                ASTNode(type="Operand", value=operand_token[1])
            ]
        )
    return None
