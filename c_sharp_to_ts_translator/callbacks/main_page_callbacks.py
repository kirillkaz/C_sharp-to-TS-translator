import sys
from dash import Input, Output, State

from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.lexical_analyzer.tokenizer import tokenize

from c_sharp_to_ts_translator.parser import Parser
from c_sharp_to_ts_translator.parser.utils import ast_to_string

# чо ета? :3
@app.callback(
    Output("to-textarea-id", "value"),
    Input("translate-button-id", "n_clicks"),
    State("from-textarea-id", "value"),
    prevent_initial_call=True,
)





def translate_callback(_: int, from_value: str) -> str:
    """Колбек для трансляции языка C# в TS

    Args:
        from_value (str): Код на языке C#

    Returns:
        str: Код на языке TS
    """

    tokens = tokenize(from_value)

    mockTokens = [
        ("KEYWORD", "int"),  # ключевое слово "var" (для объявления переменной)
        ("IDENTIFIER", "x"),  # имя переменной "x"
        ("OPERATOR", "="),  # оператор присваивания "="
        ("LITERAL", "10"),  # значение переменной "10"
        ("DELIMITER", ";"), # символ окончания строки ";"
        ("KEYWORD", "int"),  # ключевое слово "var" (для объявления переменной)
        ("IDENTIFIER", "y"),  # имя переменной "x"
        ("OPERATOR", "="),  # оператор присваивания "="
        ("LITERAL", "20"),  # значение переменной "10"
        ("DELIMITER", ";")  # символ окончания строки ";"
    ]

    mockClass = [
    ('KEYWORD', 'class'),          # class
    ('IDENTIFIER', 'MyClass'),     # MyClass
    ('DELIMITER', '{'),            # {
    ('KEYWORD', 'int'),            # int
    ('IDENTIFIER', 'x'),           # x
    ('OPERATOR', '='),             # =
    ('LITERAL', '10'),             # 10
    ('DELIMITER', ';'),            # ;
    ('DELIMITER', '}')             # }
    ]
    
    parser = Parser(tokens)
    ast = parser.parse_to_AST()

    return ast_to_string(ast)
