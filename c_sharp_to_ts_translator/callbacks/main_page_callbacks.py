from typing import Tuple

from dash import Input, Output, State, no_update

from c_sharp_to_ts_translator.app import app

from ..lexical_analyzer.tokenizer import tokenize
from ..parser import parse_to_AST

@app.callback(
    Output("timer", "n_intervals"),
    Output("timer", "interval"),
    Output("timer", "disabled"),
    Input("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def debounce_callback(_: int) -> Tuple[int, int, bool]:
    return 0, 1000, False


@app.callback(
    Output("result", "data"),
    Input("timer", "n_intervals"),
    State("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def translate_callback(trigger: int, value: str) -> str:
    """Колбэк для трансляции кода"""
    if trigger == 2:
        tokens = tokenize(value)
        AST_tree = parse_to_AST(tokens)
        # todo: generate code

        return AST_tree
    return no_update


@app.callback(
    Output("to-textarea-id", "value"),
    Input("translate-button-id", "n_clicks"),
    State("result", "data"),
    prevent_initial_call=True,
)
def print_result_callback(_: int, result: str) -> str:
    """Колбэк вывода результата

    Args:
        result (str): результат трансляции

    Returns:
        str: результат трансляции
    """
    return result
