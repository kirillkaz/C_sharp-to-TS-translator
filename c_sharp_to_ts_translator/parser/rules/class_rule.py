from ..ASTNode import ASTNode
from .declaration_rule import parse_variable_declaration
from .code_block_rule import parse_code_block  # Импортируем функцию парсинга блоков кода

def parse_class(tokens, position):
    # Проверяем, что начался класс
    if tokens[position][0] == "KEYWORD" and tokens[position][1] == "class":
        # Получаем имя класса
        class_name = tokens[position + 1][1] if tokens[position + 1][0] == "IDENTIFIER" else None
        
        if not class_name:
            raise SyntaxError(f"Expected class name at position {position + 1}")
        
        # Проверяем открытие тела класса
        if tokens[position + 2][0] != "DELIMITER" or tokens[position + 2][1] != "{":
            raise SyntaxError(f"Expected '{{' after class name at position {position + 2}")
        
        # Парсим тело класса с использованием нового парсера для блоков кода
        block_node, position = parse_code_block(tokens, position + 2)  # Пропускаем '{'
        
        # Создаем узел AST для класса
        ast_node = ASTNode(
            type="Class",
            value=class_name,
            children=block_node.children  # Тело класса уже распарсено
        )

        # Возвращаем AST и новую позицию
        return ast_node, position

    return None, position
