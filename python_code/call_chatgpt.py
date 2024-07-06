import sys
from openai import OpenAI

client = OpenAI(api_key='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')

def call_gpt3(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=True
    )
    return response

if __name__ == "__main__":
    prompt = sys.argv[1]
    response = call_gpt3(prompt)
    for chunk in response:
        if 'choices' in chunk:
            chunk_text = chunk['choices'][0].get('delta', {}).get('content', '')
            print(chunk_text, end='', flush=True)
