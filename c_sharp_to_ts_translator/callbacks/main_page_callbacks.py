import requests
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


# Колбэк для кнопки "Форматировать"
@app.callback(
    Output("from-textarea-id", "value"),
    Input("format-button-id", "n_clicks"),
    State("from-textarea-id", "value"),
    prevent_initial_call=True,
)
def format_code(n_clicks: int, code: str) -> str:
    """Колбэк для форматирования кода с использованием внешнего API"""
    if n_clicks is not None and n_clicks > 0:
        url = "https://playground.csharpier.com/Format"
        headers = {
            "accept": "*/*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://playground.csharpier.com",
            "priority": "u=1, i",
            "referer": "https://playground.csharpier.com",
            "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }
        payload = {
            "code": code,
            "printWidth": 100,
            "indentSize": 4,
            "useTabs": False,
            "parser": "CSharp"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            formatted_code = response_data.get('code', '')
            print("Форматированный код:", formatted_code)
            return formatted_code
        else:
            print("Ошибка при форматировании:", response.status_code, response.text)
            return no_update

    return no_update


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
