from openai import OpenAI
from .api_key import api_key

def get_openai_response(source_code, model="gpt-4"):
    client = OpenAI(api_key=api_key)

    prompt = f'''
        Imagine you are c# to typescript translator. Translate the code from C# to TypeScript. 1) Return the translated code. Do not write any comments, explanations or introductory words. Just the code. 2)   3) For the same code, give the same result 4) Return simple text, not markdown. 5) always explicitly specify the types. 6) Always keep the original formatting. If you get the same code several times in a row, then you should give the same result that you gave the first time. 7) Don't try to refine or think through the code, leave the entire sequence and titles as they were in the original.
        {source_code}
        '''

    response = client.chat.completions.create(
        model=model,
        store=True,
        messages = [
            {"role": "system", "content": "You are a translator from C# to TypeScript. Your task is to accept the C# code and return its TypeScript equivalent."},
            {"role": "user", "content": prompt}
        ]       
    )

    return response.choices[0].message.content


















