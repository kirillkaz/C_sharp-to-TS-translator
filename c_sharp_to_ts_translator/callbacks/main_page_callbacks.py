from typing import Tuple

from dash import Input, Output, State, no_update

from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.callback import tokenize
from c_sharp_to_ts_translator.parser import parse_to_AST
from c_sharp_to_ts_translator.code_generator.generator import generate

@app.callback(
    Output("timer", "n_intervals"),
    Output("timer", "interval"),
    Output("timer", "disabled"),
    Input("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def debounce_callback(_: int) -> Tuple[int, int, bool]:
    """колбэк для сброса задержки запроса"""

    return 0, 1000, False


@app.callback(
    Output("result", "data"),
    Input("timer", "n_intervals"),
    State("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def translate_callback(trigger: int, value: str) -> str:
    """Колбэк для трансляции кода (работает с задержкой)
    """
    if trigger == 2:
        tokens = tokenize(value)
        ast = parse_to_AST(tokens)
        code = generate(ast)
        return tokens
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
