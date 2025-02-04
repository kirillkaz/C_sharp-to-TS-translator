def join_with_separator(nodes, separator):
    """Объединяет список узлов в строку через указанный разделитель."""
    return separator.join(filter(None, [handle_node(node) for node in nodes]))

from .generator import handle_node
