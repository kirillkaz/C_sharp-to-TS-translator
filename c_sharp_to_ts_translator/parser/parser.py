from .rules import (
    parse_variable_declaration,
    parse_method_call,
    parse_operator,
    parse_literal,
    parse_string,
    parse_delimiter,
    parse_identifier,
    parse_contextual_keyword,
    parse_namespace,
    parse_class_declaration,
    parse_function_declaration,
    parse_if_statement,
    parse_else_statement,
    parse_for_loop,
    parse_while_loop,
    parse_try_catch,
    parse_switch_statement,
    parse_case_statement,
    parse_return_statement,
    parse_assignment,
    parse_expression,
    parse_array_access,
    parse_object_access
)

TOKEN_HANDLERS = {
    "KEYWORD": parse_variable_declaration,
    "STANDART_METHODS": parse_method_call,
    "OPERATOR": parse_operator,
    "LITERAL": parse_literal,
    "STRING": parse_string,
    "DELIMITER": parse_delimiter,
    "IDENTIFIER": parse_identifier,
    "CONTEXTUAL_KEYWORD": parse_contextual_keyword,
    "NAMESPACE": parse_namespace,
    "CLASS_DECLARATION": parse_class_declaration,
    "FUNCTION_DECLARATION": parse_function_declaration,
    "IF_STATEMENT": parse_if_statement,
    "ELSE_STATEMENT": parse_else_statement,
    "FOR_LOOP": parse_for_loop,
    "WHILE_LOOP": parse_while_loop,
    "TRY_CATCH": parse_try_catch,
    "SWITCH_STATEMENT": parse_switch_statement,
    "CASE_STATEMENT": parse_case_statement,
    "RETURN_STATEMENT": parse_return_statement,
    "ASSIGNMENT": parse_assignment,
    "EXPRESSION": parse_expression,
    "ARRAY_ACCESS": parse_array_access,
    "OBJECT_ACCESS": parse_object_access
}

def parse_to_AST(tokens):
    if isinstance(tokens, str):
        return tokens

    nodes = []
    position = 0

    while position < len(tokens):
        token_type, token_value = tokens[position]

        if token_type in TOKEN_HANDLERS:
            handler = TOKEN_HANDLERS[token_type]
            nodes.append(handler(tokens, position))
        else:
            if token_type not in ["WHITESPACE", "COMMENT"]:
                print(f"Неизвестный токен: {token_type} -> {token_value}")

        position += 1

    return ASTNode(
        type="Program",
        children=nodes
    )
