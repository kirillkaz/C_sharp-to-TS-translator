import re

# Определим шаблоны для различных токенов C#
TOKENS = [
    ('KEYWORD', r'\b(public|private|class|void|int|float|string|bool)\b'),
    ('IDENTIFIER', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
    ('OPERATOR', r'(\+|\-|\*|\/|==|!=|&&|\|\|)'),
    ('LITERAL', r'\b\d+(\.\d+)?\b'),  # числа
    ('STRING', r'"[^"]*"'),           # строки
    ('DELIMITER', r'(\{|\}|\(|\)|;|,)')
]

# Токенизатор
def tokenize(code):
    tokens = []
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
            raise SyntaxError(f"Неизвестный токен: '{code[pos]}' в позиции {pos}")
            pos += 1
    return tokens