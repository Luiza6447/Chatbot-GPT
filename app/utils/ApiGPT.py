import requests
import json
import os

def chatGPT(message, contexto):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer CHAVE API AKI',
        'Content-Type': 'application/json'
    }

    data = {
        'messages': contexto,
        'model': 'gpt-3.5-turbo'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    responseJson = response.json()

    try:
        if responseJson['choices'] and len(responseJson['choices']) > 0:
            retornoApi = responseJson['choices'][0]['message']['content']
            return retornoApi
        else:
            return None
    except:
        return None