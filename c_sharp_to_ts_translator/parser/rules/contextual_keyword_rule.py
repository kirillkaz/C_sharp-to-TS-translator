from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier
from .literal_rule import parse_literal
from .operator_rule import parse_operator

def parse_contextual_keyword(tokens, position):
    if position + 1 >= len(tokens):
        return None

    token = tokens[position]

    if token[0] == "CONTEXTUAL_KEYWORD":
        value = token[1]
        
        # Пример обработки контекстных ключевых слов (например, "add", "remove")
        if value in ["add", "remove", "update"]:
            return ASTNode(
                type="ContextualKeyword",
                value=value
            )
        return None
    return None
