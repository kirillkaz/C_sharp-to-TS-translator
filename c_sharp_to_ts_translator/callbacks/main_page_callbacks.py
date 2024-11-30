from dash import Input, Output, State

from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.lexical_analyzer.tokenizer import tokenize
from c_sharp_to_ts_translator.AST_builder import AST_builder
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


    # tokens = tokenize(from_value)
    # int x = 42;
    tokens = [
    ("KEYWORD", "int"),
    ("IDENTIFIER", "x"),
    ("ASSIGNMENT", "="),
    ("NUMBER", "42"),
    ("SEMICOLON", ";")
    ]
    
    AST_tree = AST_builder(tokens)
    

    return AST_tree
