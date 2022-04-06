import requests
import json
import string

def retrieve_message(channel_id):
    headers = {
        'authorization' : ''
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=150', headers=headers)
    jsonn = json.loads(r.text)
    counter = 0 
    for word in jsonn:
        dict = word['author']
        text = word['content']
        attachment = word['attachments']
        if 'MEE6' not in dict.values():
            if len(attachment) == 0:
                if text[0] != '<':
                    print(text)

retrieve_message('877375592369111160')
