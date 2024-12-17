from dash import Input, Output, State

from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.lexical_analyzer.tokenizer import tokenize
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

    tokens = tokenize(from_value)
    

    return from_value + "ti krasavchik (roma loh)"
