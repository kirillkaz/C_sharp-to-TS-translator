from ..ASTNode import ASTNode
from .declaration_rule import parse_variable_declaration
from .standart_methods_rules import parse_standard_method_call
from .expression_rule import parse_expression


def parse_method_call(tokens, position):
    """
    Парсер для вызова методов, включая стандартные методы, такие как Console.WriteLine(...).
    """
    token_type, token_value = tokens[position]

    # Проверяем, что это стандартный метод или пользовательский метод
    if token_type not in {"STANDART_METHODS", "IDENTIFIER"}:
        raise SyntaxError(f"Ожидался идентификатор метода на позиции {position}, получено {token_type}")

    method_name = token_value  # Имя метода
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


def parse_code_block(tokens, position):
    if tokens[position][1] != "{":
        raise SyntaxError("Ожидалась открывающая фигурная скобка")
    
    position += 1  # Пропускаем '{'
    block_node = ASTNode(type="CodeBlock", children=[])
    
    while position < len(tokens) and tokens[position][1] != "}":
        token_type, token_value = tokens[position]
        
        node = None  # Инициализируем node как None перед каждой итерацией
        
        if token_type == "KEYWORD" and token_value in {"int", "string", "float", "double"}:  # Пример: объявление переменной
            node, position = parse_variable_declaration(tokens, position)
        elif token_type == "KEYWORD" and token_value in {"static", "public", "private"}:  # Объявление метода
            node, position = parse_method_declaration(tokens, position)
        elif token_type == "IDENTIFIER":  # Пример: вызов метода
            node, position = parse_method_call(tokens, position)
        elif token_type == "STANDART_METHODS":  # Обрабатываем стандартные методы
            node, position = parse_standard_method_call(tokens, position)
        elif token_type == "KEYWORD" and token_value == "return":  # Обрабатываем return
            position += 1;
            expr_node, position = parse_expression("any", tokens, position)
            position += 1;
            node = ASTNode(type="ReturnStatement", children=[expr_node])
        else:
            raise SyntaxError(f"Неизвестный токен: {token_type}, {token_value}, {position}")
        
        if node:  # Добавляем только если node был корректно инициализирован
            block_node.children.append(node)
    
    if position >= len(tokens) or tokens[position][1] != "}":
        raise SyntaxError("Ожидалась закрывающая фигурная скобка")
    
    return block_node, position + 1


def parse_method_declaration(tokens, position):
    """
    Парсер для объявления методов, включая тип возвращаемого значения, параметры и тело.
    Пример: static void Add(string a, string b) { return a + b; }
    """
    modifiers = []  # Модификаторы (например, static, public)
    while tokens[position][0] == "KEYWORD" and tokens[position][1] in {"static", "public", "private"}:
        modifiers.append(tokens[position][1])
        position += 1

    # Ожидаем возвращаемый тип метода
    if tokens[position][0] != "KEYWORD":
        raise SyntaxError(f"Ожидался тип возвращаемого значения на позиции {position}")
    return_type = tokens[position][1]
    position += 1

    # Ожидаем имя метода
    if tokens[position][0] != "IDENTIFIER":
        raise SyntaxError(f"Ожидалось имя метода на позиции {position}")
    method_name = tokens[position][1]
    position += 1

    # Ожидаем открывающую скобку для аргументов
    if tokens[position][1] != "(":
        raise SyntaxError(f"Ожидалась '(' после имени метода на позиции {position}")
    position += 1

    # Парсим аргументы метода
    parameters = []
    while position < len(tokens) and tokens[position][1] != ")":
        token_type, token_value = tokens[position]

        if token_type in {"KEYWORD", "IDENTIFIER"}:  # Тип аргумента и его имя
            param_type = token_value
            position += 1
            if tokens[position][0] != "IDENTIFIER":
                raise SyntaxError(f"Ожидалось имя аргумента после типа {param_type} на позиции {position}")
            param_name = tokens[position][1]
            parameters.append(ASTNode(type="Parameter", value=(param_type, param_name)))
            position += 1
        elif token_type == "DELIMITER" and token_value == ",":  # Пропускаем запятые
            position += 1
        else:
            raise SyntaxError(f"Некорректный токен в аргументах метода: {token_type}, {token_value}, {position}")
    
    # Проверяем закрывающую скобку
    if tokens[position][1] != ")":
        raise SyntaxError(f"Ожидалась ')' после аргументов метода на позиции {position}")
    position += 1

    # Ожидаем тело метода
    if tokens[position][1] != "{":
        raise SyntaxError(f"Ожидалась открывающая фигурная скобка на позиции {position}")
    method_body, position = parse_code_block(tokens, position)

    # Создаем узел AST для метода
    return ASTNode(
        type="MethodDeclaration",
        value=method_name,
        children=[
            ASTNode(type="Modifiers", value=modifiers),
            ASTNode(type="ReturnType", value=return_type),
            ASTNode(type="Parameters", children=parameters),
            method_body
        ]
    ), position

