from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier
from .operator_rule import parse_operator
from .literal_rule import parse_literal
from .string_rule import parse_string
from .declaration_rule import parse_variable_declaration
from .expression_rule import parse_expression

def parse_function_declaration(tokens, position):
    if position + 4 >= len(tokens):
        return None
    
    func_token, identifier_token, delimiter_token, body_token = tokens[position:position + 4]
    
    # Ожидаем структуру: return type funcName() { ... }
    if func_token[0] == "KEYWORD" and func_token[1] == "function" and delimiter_token[1] == "(":
        function_node = ASTNode(
            type="Function",
            value=identifier_token[1],
            children=[]
        )
        
        position += 1
        # Парсим аргументы функции
        while position < len(tokens):
            argument = parse_variable_declaration(tokens, position)
            if argument:
                function_node.children.append(argument)
                position += 1
            if tokens[position][1] == ")":
                break
            position += 1

        # Парсим тело функции
        body_node = []
        while position < len(tokens) and tokens[position][1] != "}":
            statement = parse_expression(tokens, position)
            if statement:
                body_node.append(statement)
                position += 1
        function_node.children.append(ASTNode(type="FunctionBody", children=body_node))
        return function_node
    return None
