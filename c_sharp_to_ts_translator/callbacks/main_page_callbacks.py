import sys
from dash import Input, Output, State

from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.lexical_analyzer.tokenizer import tokenize

from c_sharp_to_ts_translator.parser import parse_to_AST
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

    tokens = [
        ("KEYWORD", "var"),  # ключевое слово "var" (для объявления переменной)
        ("IDENTIFIER", "x"),  # имя переменной "x"
        ("OPERATOR", "="),  # оператор присваивания "="
        ("NUMBER", "10"),  # значение переменной "10"
        ("SEMICOLON", ";")  # символ окончания строки ";"
    ]
    
    ast = parse_to_AST(tokens)

    return ast_to_string(ast)
