import re

# Определим шаблоны для различных токенов C#
TOKENS = [
    ('KEYWORD', r'\b(public|private|class|void|int|float|string|bool)\b'),
    ('IDENTIFIER', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
    ('OPERATOR', r'(\+|\-|\*|\/|==|!=|&&|\|\||=)'),
    ('LITERAL', r'\b\d+(\.\d+)?\b'),  # числа
    ('STRING', r'"[^"]*"'),           # строки
    ('DELIMITER', r'(\{|\}|\(|\)|;|,)')
]

# Предварительная обработка кода
def preprocess_code(code):
    # Добавляем пробелы вокруг знаков, которые выступают разделителями
    # Это поможет токенизатору корректно интерпретировать код
    delimiters = "{}();,"
    for delimiter in delimiters:
        code = code.replace(delimiter, f' {delimiter} ')
    # Заменяем множественные пробелы одним пробелом, чтобы избежать лишних пустых токенов
    code = re.sub(r'\s+', ' ', code)
    return code.strip()

# Токенизатор
def tokenize(code):
    tokens = []
    code = preprocess_code(code)  # Предварительная обработка кода
    pos = 0
    while pos < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                token_text = match.group(0)
                tokens.append((token_type, token_text))
                pos = match.end(0)
                break
        if not match:
            # Если токен не найден, это ошибка лексического анализа
            raise SyntaxError(f"Неизвестный токен: '{code[pos]}' в позиции {pos}")
        pos += 1
    return tokens
