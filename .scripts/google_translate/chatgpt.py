import json
import requests

def translate(api_key, ipt):
    prompt = f'假設你是一位python工程師，請將下列文件翻譯為繁體中文 “{ipt}”'
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        },
        json = {
            'model': 'text-davinci-003',
            'prompt': prompt,
            'temperature': 0.4,
            'max_tokens': 1000
        }
    )
    return response

def Translator(ipt, api_key):
    response = translate(api_key, ipt)
    opt = json.loads(response.text)['choices'][0]['text']
    print(opt)