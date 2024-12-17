from c_sharp_to_ts_translator.app import app
from c_sharp_to_ts_translator.callbacks import translate_callback
from c_sharp_to_ts_translator.layouts.main_layout import render_main_page


def main() -> None:
    """Точка входа в приложение"""
    app.layout = render_main_page()
    app.run(debug=True)


if __name__ == "__main__":
    main()
