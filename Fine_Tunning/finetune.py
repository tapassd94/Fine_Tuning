import openai
import os
import requests

with open('C:/Users/TapasSaha/Desktop/Fine_Tunning/openaiapikey.txt', 'r') as infile:
    open_ai_api_key = infile.read()

print(open_ai_api_key)
openai.api_key = open_ai_api_key


def file_upload(filename, purpose='fine-tune'):
    resp = openai.File.create(purpose=purpose, file=open(filename))
    return resp


def finetune_model(fileid, suffix, model='davinci'):
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % open_ai_api_key}
    payload = {'training_file': fileid, 'model': model, 'suffix': suffix}
    resp = requests.request(method='POST', url='https://api.openai.com/v1/fine-tunes', json=payload, headers=header, timeout=45)
    return resp


def finetune_get(fine_tune_id, promt, model):
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % open_ai_api_key}
    params = {'prompt': promt, 'model': model}
    response = requests.request(method='GET', url=f"https://api.openai.com/v1/fine-tunes/{fine_tune_id}/completions", params=params, headers=header, timeout=45)
    data = response.json()["choices"][0]["text"]
    print(data)


resp = file_upload('C:/Users/TapasSaha/Desktop/Fine_Tunning/data.jsonl')
print(resp)
ft_resp = finetune_model(resp['id'], 'basketball_info', 'davinci')
print(ft_resp.json())

