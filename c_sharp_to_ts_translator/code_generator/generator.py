from .node_handlers.expressions import handle_expression, handle_variable_declaration, handle_assignment_expression
from .node_handlers.statements import handle_statement, handle_if_statement, handle_else_statement, handle_for_loop, handle_while_loop, handle_try_catch
from .node_handlers.methods import handle_method_call
from .node_handlers.classes import handle_class_declaration, handle_function_declaration, handle_namespace
from .node_handlers.objects import handle_array_access, handle_object_access
from .node_handlers.literals import handle_literal

def generate(ast):
    """Главная функция генерации кода TypeScript из AST."""
    if not ast:
        return ""
    return handle_node(ast)


def handle_node(node):
    """Обрабатывает узел AST и вызывает нужный обработчик."""
    if node.type == "Program":
        return "\n".join([handle_node(child) for child in node.children])
    elif node.type == "VariableDeclaration":
        return handle_variable_declaration(node)
    elif node.type == "AssignmentExpression":
        return handle_assignment_expression(node)
    elif node.type == "MethodCall":
        return handle_method_call(node)
    elif node.type == "IfStatement":
        return handle_if_statement(node)
    elif node.type == "ElseStatement":
        return handle_else_statement(node)
    elif node.type == "ForLoop":
        return handle_for_loop(node)
    elif node.type == "WhileLoop":
        return handle_while_loop(node)
    elif node.type == "TryCatch":
        return handle_try_catch(node)
    elif node.type == "ClassDeclaration":
        return handle_class_declaration(node)
    elif node.type == "FunctionDeclaration":
        return handle_function_declaration(node)
    elif node.type == "Namespace":
        return handle_namespace(node)
    elif node.type == "ArrayAccess":
        return handle_array_access(node)
    elif node.type == "ObjectAccess":
        return handle_object_access(node)
    elif node.type in ["Number", "String", "Boolean"]:
        return handle_literal(node)
    else:
        raise ValueError(f"Неизвестный тип узла: {node.type}")
