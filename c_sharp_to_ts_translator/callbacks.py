from dash import Input, Output, State, callback_context
import traceback  # Для получения текста исключения

# Предположим, функция трансляции вызывает исключение
from c_sharp_to_ts_translator.translator import translate_csharp_to_ts
from dash.exceptions import PreventUpdate


def register_callbacks(app):
    """Регистрируем колбэки приложения"""

    @app.callback(
        Output("to-textarea-id", "value"),
        Output("error-alert", "children"),
        Output("error-alert", "is_open"),
        Input("translate-button-id", "n_clicks"),
        State("from-textarea-id", "value"),
        prevent_initial_call=True
    )
    def translate_callback(n_clicks, csharp_code):
        """Колбэк для трансляции кода"""
        try:
            # Попытка трансляции кода
            ts_code = translate_csharp_to_ts(csharp_code)
            return ts_code, "", False  # Очищаем алерт при успешном выполнении
        except Exception as e:
            # В случае исключения отправляем сообщение в алерт
            error_message = f"Ошибка: {str(e)}"
            print(traceback.format_exc())  # Логирование стека исключения
            return "", error_message, True
