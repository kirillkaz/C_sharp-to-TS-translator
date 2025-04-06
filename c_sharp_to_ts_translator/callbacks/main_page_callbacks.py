from typing import Tuple
from dash import Input, Output, State, no_update
from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.test import tokenize
from c_sharp_to_ts_translator.parser import parse_to_AST

def generate(val):
    return val

@app.callback(
    Output("timer", "n_intervals"),
    Output("timer", "interval"),
    Output("timer", "disabled"),
    Input("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def debounce_callback(_: int) -> Tuple[int, int, bool]:
    """Колбэк для сброса задержки запроса"""
    return 0, 1000, False


@app.callback(
    Output("result", "data"),
    Input("timer", "n_intervals"),
    State("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def translate_callback(trigger: int, value: str) -> str:
    """Колбэк для трансляции кода (работает с задержкой)"""
    if trigger == 2:
        tokens = tokenize(value)
        ast = parse_to_AST(tokens)
        code = generate(ast)
        return code
    return no_update


@app.callback(
    Output("to-textarea-id", "value"),
    Input("translate-button-id", "n_clicks"),
    State("result", "data"),
    prevent_initial_call=True,
)
def print_result_callback(_: int, result: str) -> str:
    """Колбэк вывода результата"""
    return result


# Колбэк для управления кнопкой копирования и уведомлением
@app.callback(
    Output("copy-button-id", "disabled"),  # Управление состоянием кнопки
    Output("copy-status", "is_open"),  # Уведомление
    Input("copy-button-id", "n_clicks"),
    State("to-textarea-id", "value"),
    prevent_initial_call=True,
)
def copy_to_clipboard(n_clicks: int, textarea_value: str) -> Tuple[bool, bool]:
    """Копирование в буфер обмена и управление кнопкой"""
    if textarea_value:
        if n_clicks is not None and n_clicks > 0:
            # Показываем уведомление "Скопировано в буфер"
            return False, True  # Кнопка активна, уведомление показывается
        return False, False  # Кнопка активна, уведомление не показывается
    return True, False  # Кнопка заблокирована, уведомление не показывается
