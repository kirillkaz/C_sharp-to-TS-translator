from openai import OpenAI
from .api_key import api_key
from functools import lru_cache

def is_brackets_balanced(s: str) -> bool:
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in s:
        if char in brackets:  # Открывающая скобка
            stack.append(char)
        elif char in brackets.values():  # Закрывающая скобка
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack  # Если стек пуст, скобки сбалансированы

@lru_cache(maxsize=100)
def tokenize(source_code, model="gpt-4"):
    if not is_brackets_balanced(source_code):
        return "SyntaxError"

    print(source_code)
    client = OpenAI(api_key=api_key)    

    prompt = f'''
        Imagine you are c# to typescript translator. Translate the code from C# to TypeScript. 1) Return the translated code. Do not write any comments, explanations or introductory words, just the code. 2) If the input code contains syntax errors, just return the text "SyntaxError"  3) For the same code, give the same result 4) Return simple text, not markdown. 5) always explicitly specify the types. 6) Always keep the original formatting. If you get the same code several times in a row, then you should give the same result that you gave the first time. 7) Don't try to refine or think through the code, leave the entire 8) sequence and titles as they were in the original. 9)If the request differs by at least one character from the previous request, these changes should be reflected in the response. 10) In output typescript code should not contain namespace and call. The entire class hierarchy of the source program must be repeated in the output typescript code. Output typescript code should alwayd contain Program class. Output code should not contain Program.main([]);
        {source_code}
        '''

    response = client.chat.completions.create(
        model=model,
        store=True,
        messages = [
            {"role": "system", "content": "You are a translator from C# to TypeScript. Your task is to accept the C# code and return its TypeScript equivalent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content