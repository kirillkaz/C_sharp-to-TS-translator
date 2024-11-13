import dash_bootstrap_components as dbc
from dash import html


def _render_texareas_block() -> html.Div:
    """Функция для отрисовки блока с текстовыми полями"""
    return html.Div(
        [
            dbc.Textarea(
                id="from-textarea-id",
                placeholder="Введите код для на C# для трансляции...",
                className="from-textarea",
                value="int a = 2;\nint b = 5;\nint c = a + b;"
            ),  
            dbc.Textarea(
                id="to-textarea-id",
                placeholder="Здесь появится код на TypeScript...",
                className="to-textarea",
                readOnly=True,
            ),
        ],
        className="textareas-block",
    )


def _render_button_block() -> html.Div:
    """Функция для отрисовки блока с кнопкой транслятора"""
    return html.Div(
        [
            dbc.Button(
                id="translate-button-id",
                className="translate-button",
                children="Транслировать код!",
                color="primary",
            )
        ],
        className="translate-button-block",
    )


def render_main_page() -> html.Div:
    """Главный layout"""
    return html.Div(
        [
            _render_texareas_block(),
            _render_button_block(),
        ]
    )
