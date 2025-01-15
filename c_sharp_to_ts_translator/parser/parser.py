from .rules import parse_variable_declaration
from .rules import parse_class
from .ASTNode import ASTNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse_to_AST(self):
        nodes = []

        while self.position < len(self.tokens):
            token_type, token_value = self.tokens[self.position]

            if token_type == "KEYWORD" and token_value == "class":
                node, new_pos = parse_class(self.tokens, self.position)  # Используем функцию parse_class
                nodes.append(node)
                self.position = new_pos
            elif token_type == "KEYWORD" and token_value in {"int", "double", "float", "bool", "string", "char"} :
                node, new_pos = parse_variable_declaration(self.tokens, self.position)
                nodes.append(node)
                self.position = new_pos
            else:
                self.position += 1  # Перемещаем позицию для остальных случаев

        return ASTNode(
            type="Program",
            children=nodes
        )
