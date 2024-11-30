class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

# Основная функция парсера
def AST_builder(tokens):
    # Шаг 1: Разделение токенов на блоки переменных
    declarations = parse_variable_declarations(tokens)
    
    # Шаг 2: Построение корневого узла AST
    return ASTNode(
        type="Program",
        children=declarations
    )

# Функция для парсинга деклараций переменных
def parse_variable_declarations(tokens):
    declarations = []
    while tokens:
        declaration = parse_variable_declaration(tokens)
        if declaration:
            declarations.append(declaration)
        # Удаляем уже обработанные токены
        tokens = tokens[len(declaration.children):]
    return declarations

# Функция для парсинга одной декларации переменной
def parse_variable_declaration(tokens):
    if len(tokens) < 4:
        return None
    
    # Ожидаем структуру: type identifier = value ;
    type_token, identifier_token, assignment_token, value_token, semicolon_token = tokens[:5]
    
    # Проверка на корректность структуры
    if type_token[0] == "KEYWORD" and assignment_token[0] == "ASSIGNMENT" and semicolon_token[0] == "SEMICOLON":
        # Создание AST для переменной
        return ASTNode(
            type="VariableDeclaration",
            value=identifier_token[1],
            children=[
                ASTNode(type="Type", value=type_token[1]),
                ASTNode(type="Value", value=parse_value(value_token))
            ]
        )
    return None

# Функция для парсинга значения (число или строка)
def parse_value(token):
    if token[0] == "NUMBER":
        return int(token[1])
    elif token[0] == "STRING":
        return token[1][1:-1]  # Убираем кавычки
    return None