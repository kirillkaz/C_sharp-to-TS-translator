import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_html_components as html

def _render_texareas_block() -> html.Div:
    """Функция для отрисовки блока с текстовыми полями"""
    return html.Div(
        [
            dbc.Textarea(
                id="from-textarea-id",
                placeholder="Введите код на C# для трансляции...",
                className="from-textarea",
            ),
            dbc.Textarea(
                id="to-textarea-id",
                placeholder="Здесь появится код на TypeScript...",
                className="to-textarea",
                readOnly=True,
            ),
            dcc.Interval(id="timer", interval=2000, max_intervals=2, disabled=True),
            dcc.Store(id="result", storage_type="session"),
        ],
        className="textareas-block",
    )


def _render_button_block() -> html.Div:
    """Функция для отрисовки блока с кнопкой транслятора"""
    return html.Div(
        [
            dbc.Button(
                id="format-button-id",
                className="format-button",
                children="Форматировать",
                color="secondary",
            ),
            dbc.Button(
                id="translate-button-id",
                className="translate-button",
                children="Транслировать код!",
                color="primary",
            ),
            dcc.Clipboard(
                target_id="to-textarea-id",
                id="copy-clipboard",
                style={"marginLeft": "10px", "cursor": "pointer"}  # Отступ и курсор в виде указателя
            ),
        ],
        className="translate-button-block",
        style={
            "display": "flex",  # Flexbox для горизонтального выравнивания
            "alignItems": "center",  # Выравнивание по вертикали
            "justifyContent": "center",  # Выравнивание по горизонтали
        },
    )


def _render_error_alert() -> dbc.Alert:
    """Функция для блока отображения ошибок"""
    return dbc.Alert(
        id="error-alert",
        children="Произошла ошибка!",
        color="danger",
        dismissable=True,  # Позволяет закрыть плашку
        is_open=False,  # Изначально скрыта
        className="error-alert",
    )


def render_main_page() -> html.Div:
    """Главный layout"""
    return html.Div(
        [
            _render_texareas_block(),
            _render_button_block(),
            _render_error_alert(),  # Добавляем блок для ошибок
            dbc.Alert(
                "Текст скопирован в буфер обмена",
                id="copy-status",
                color="success",
                is_open=False,
                duration=2000,
                dismissable=True,
            ),
        ]
    )
