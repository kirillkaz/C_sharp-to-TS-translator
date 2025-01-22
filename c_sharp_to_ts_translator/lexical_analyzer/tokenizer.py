import re
from .tests.callback import tokenize

TOKENS = [
    ('KEYWORD', r'\b(break|byte|case|catch|char|const|continue|delegate|do|double|enum|false|float|true|foreach|in|int|interface|long|namespace|new|null|object|operator|private|public|private|protected|short|static|string|struct|switch|this|throw|try|using|void|class|if|else|return|for|while)\b'),
    ('CONTEXTUAL_KEYWORD', r'\b(add|and|args|dynamic|equals|global|nameof|not|remove|set|value|var|with)\b|:'),
    ("STANDART_METHODS",r'\b(Console\.WriteLine)\b'),
    ('IDENTIFIER', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
    ('OPERATOR', r'(\+|\-|\*|\/|==|!=|&&|\|\||\||&|=|>|<|>=|<=|\+-|\-=|\*=|\/=|\%=|\+\+|\-\-)'),   
    ('LITERAL', r'\b\d+(\.\d+)?\b'),  # Числа с поддержкой десятичной точки
    ('STRING', r'"([^"\\]|\\.)*"'),   # Строки с обработкой escape-последовательностей
    ('DELIMITER', r'(\{|\}|\(|\)|;|,|\.|\[|\])'),
    ('WHITESPACE', r'\s+|[\r\n]+'),           # Пробелы
    ('COMMENT', r'\/\/[^\n]*|\/\*[\s\S]*?\*\/'),  # Однострочные и многострочные комментарии
    ('UNKNOWN', r'.')                 # Любой неизвестный символ
]

# Предварительная обработка кода
def preprocess_code(code):
    # Добавляем пробелы вокруг знаков, которые выступают разделителями
    delimiters = "{}();,[]"
    for delimiter in delimiters:
        code = code.replace(delimiter, f' {delimiter} ')
    # Заменяем множественные пробелы одним пробелом, чтобы избежать лишних пустых токенов
    code = re.sub(r'\s+', ' ', code)
    return code.strip()

# Токенизатор
def tokenise(code):
    tokens = []
    code = preprocess_code(code)  # Предварительная обработка кода
    pos = 0
    line = 1  # Для отслеживания строки
    while pos < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                token_text = match.group(0)
                if token_type == "WHITESPACE":  # Игнорируем пробелы
                    pos = match.end(0)
                    line += token_text.count('\n')  # Обновляем номер строки
                    break
                if token_type == "UNKNOWN":  # Обрабатываем неизвестный символ
                    raise SyntaxError(f"Неизвестный символ '{token_text}' на строке {line}, позиции {pos}")
                if token_type == "STRING" and not token_text.endswith('"'):  # Проверка незакрытой строки
                    raise SyntaxError(f"Незакрытая строка на строке {line}, позиции {pos}")
                if token_type != "COMMENT":  # Игнорируем комментарии
                    tokens.append((token_type, token_text))
                pos = match.end(0)
                break
        if not match:
            # Если токен не найден, выбрасываем ошибку
            raise SyntaxError(f"Неизвестный токен на строке {line}, позиции {pos}: '{code[pos]}'")
    return tokens
















