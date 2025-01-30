def ast_to_string(node, indent=""):    
    result = f"{indent}{node.type}: {node.value}\n" 
    for child in node.children:
        result += ast_to_string(child, indent + "  ")  # Увеличиваем отступ   
    return result