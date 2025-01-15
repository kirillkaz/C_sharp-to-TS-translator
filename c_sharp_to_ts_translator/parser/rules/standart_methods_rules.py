from ..ASTNode import ASTNode

def parse_standard_method_call(tokens, position):
    """
    Парсер для стандартных методов, таких как Console.WriteLine.
    """
    token_type, token_value = tokens[position]

    if token_type != "STANDART_METHODS" or token_value != "Console.WriteLine":
        return None, position  # Если не стандартный метод, возвращаем None

    method_name = "Console.WriteLine"
    position += 1

    # Проверяем наличие открывающей скобки
    if tokens[position][1] != "(":
        raise SyntaxError(f"Ожидалась '(' после имени метода на позиции {position}")
    
    position += 1  # Пропускаем '('
    args = []

    # Обрабатываем аргументы метода
    while position < len(tokens) and tokens[position][1] != ")":
        token_type, token_value = tokens[position]

        if token_type in {"LITERAL", "STRING", "IDENTIFIER"}:  # Литералы, строки или идентификаторы
            args.append(ASTNode(type=token_type, value=token_value))
        elif token_type == "OPERATOR":  # Операторы (например, "+")
            args.append(ASTNode(type="Operator", value=token_value))
        elif token_type == "DELIMITER" and token_value == ",":  # Пропускаем запятые
            position += 1
            continue
        else:
            raise SyntaxError(f"Некорректный аргумент или токен: {token_type}, {token_value} на позиции {position}")
        
        position += 1

    # Проверяем наличие закрывающей скобки
    if tokens[position][1] != ")":
        raise SyntaxError(f"Ожидалась ')' после аргументов метода на позиции {position}")
    
    position += 1  # Пропускаем ')'

    # Проверяем наличие точки с запятой
    if tokens[position][1] != ";":
        raise SyntaxError(f"Ожидалась ';' после вызова метода на позиции {position}")
    
    position += 1  # Пропускаем ';'

    # Создаем узел AST для вызова метода
    return ASTNode(type="MethodCall", value=method_name, children=args), position
