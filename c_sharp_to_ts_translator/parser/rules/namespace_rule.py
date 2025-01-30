from ..ASTNode import ASTNode
from .identifier_rule import parse_identifier
from .contextual_keyword_rule import parse_contextual_keyword
from .function_rule import parse_function_declaration

def parse_namespace(tokens, position):
    if position + 2 >= len(tokens):
        return None

    namespace_token, identifier_token, delimiter_token = tokens[position:position + 3]
    
    # Ожидаем структуру: namespace MyNamespace;
    if namespace_token[0] == "KEYWORD" and namespace_token[1] == "namespace" and delimiter_token[1] == ";":
        return ASTNode(
            type="Namespace",
            value=identifier_token[1]
        )
    return None
