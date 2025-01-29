def generate_ts_code(node, indent_level=0):
    result = ""
    
    # Функция для преобразования типов
    def map_type(type_):
        # Преобразование типов из других языков в TypeScript
        type_mapping = {
            "int": "number",
            "double": "number",
            "string": "string",
            "boolean": "boolean",
            "void": "void",
            # Здесь можно добавить другие типы по мере необходимости
        }
        return type_mapping.get(type_, type_)
    
    if node.type == "Program":
        for child in node.children:
            result += generate_ts_code(child, indent_level) + "\n"
        return result.strip()
    
    if node.type == "Class":
        class_name = node.value
        result = f"class {class_name} {{\n"
        for child in node.children:
            result += generate_ts_code(child, indent_level + 1) + "\n"
        result += "}"  # Закрывающая скобка для класса
        return result
    
    if node.type == "MethodDeclaration":
        method_name = node.value
        modifiers = " ".join([mod.value for mod in node.children if isinstance(mod.value, str)])
        return_type = next((child.value for child in node.children if child.type == "ReturnType"), None)
        
        # Убираем `void`, если метод не должен ничего возвращать
        if return_type == "void":
            return_type = "void"
        
        # Получаем параметры метода
        parameters_node = next((child for child in node.children if child.type == "Parameters"), None)
        parameters = []
        if parameters_node:
            # Преобразуем типы параметров перед генерацией
            parameters = [f"{param.value[1]}: {map_type(param.value[0])}" for param in parameters_node.children]
        
        # Получаем блок кода метода
        code_block_node = next((child for child in node.children if child.type == "CodeBlock"), None)
        code_block = generate_ts_code(code_block_node, indent_level + 1) if code_block_node else ""
        
        # Формируем сигнатуру метода
        method_code = f"{modifiers} {method_name}({', '.join(parameters)})"
        if return_type:
            method_code += f": {map_type(return_type)}"
        method_code += " {\n"
        method_code += f"{code_block}\n"
        method_code += "}"  # Закрывающая скобка метода
        return method_code
    
    if node.type == "Modifiers":
        return " ".join([mod.value for mod in node.children if isinstance(mod.value, str)])
    
    if node.type == "VariableDeclaration":
        type_ = None
        identifier = None
        value = None
        
        for child in node.children:
            if child.type == "Type":
                type_ = child.value
            elif child.type == "Identifier":
                identifier = child.value
            elif child.type == "Value":
                if child.children:
                    value = generate_ts_code(child.children[0], indent_level)
        
        # Преобразуем типы
        type_ = map_type(type_)
        
        if value:
            return f"let {identifier}: {type_} = {value};"
        return f"let {identifier}: {type_};"
    
    if node.type == "Literal":
        return str(node.value)
    
    if node.type == "BinaryExpression":
        if len(node.children) != 3:
            raise SyntaxError(f"Unexpected BinaryExpression structure: {str(node)}")
        
        left_operand = node.children[0]
        operator = node.children[1]
        right_operand = node.children[2]
        
        left = generate_ts_code(left_operand, indent_level)
        operator_value = operator.value
        right = generate_ts_code(right_operand, indent_level)
        
        return f"({left} {operator_value} {right})"
    
    if node.type == "LeftOperand" or node.type == "RightOperand":
        if node.children:
            return generate_ts_code(node.children[0], indent_level)
        return node.value
    
    if node.type == "Parameter":
        return f"{node.value[1]}: {map_type(node.value[0])}"
    
    if node.type == "ReturnStatement":
        return f"return {generate_ts_code(node.children[0], indent_level)};"
    
    if node.type == "CodeBlock":
        result = ""
        for child in node.children:
            result += generate_ts_code(child, indent_level + 1) + "\n"
        return result.strip()

    print(f"Unexpected node type: {node.type}, value: {node.value}, children: {node.children}")
    
    raise SyntaxError(f"Unexpected AST node type or structure: {str(node)}")
