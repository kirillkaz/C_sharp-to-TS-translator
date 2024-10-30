import dash_bootstrap_components as dbc
from dash_extensions.enrich import (
    Dash,
    DashProxy,
    MultiplexerTransform,
    NoOutputTransform,
)
from flask import Flask


def make_app() -> Dash:
    """Функция для создания приложения Dash

    Returns:
        Dash: Приложение Dash
    """
    server = Flask(__name__)

    app = DashProxy(
        __name__,
        transforms=[MultiplexerTransform(), NoOutputTransform()],
        external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
        server=server,
        suppress_callback_exceptions=True,
        assets_folder="./assets",
    )

    return app


app = make_app()
