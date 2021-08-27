import json
import requests
from starlette.responses import RedirectResponse
from Data.connection import Table


def get_supervisor_chat_id(email: str):
    table = Table('users')
    user = table.query('RowKey', f'{email}')
    return user.items[0]['SupervisorGoogleChatID']

def prepare_bot_message(_json):
    email = _json['PartitionKey']
    badge_requests_list = '\n- '.join([badge['title'] for badge in _json['requests']])
    supervisor_id = get_supervisor_chat_id(email)
    if supervisor_id == '':
        return f'Incoming badge application!\n\n*User*: {email}\n*Badges*:\n- {badge_requests_list}'
    elif supervisor_id == ' ':
        return f'Incoming badge application!\n\n*User*: {email}\n*Badges*:\n- {badge_requests_list}'
    elif supervisor_id is None:
        return f'Incoming badge application!\n\n*User*: {email}\n*Badges*:\n- {badge_requests_list}'
    else:
        return f'<users/{supervisor_id}> Incoming badge application!\n\n*User*: {email}\n*Badges*:\n- {badge_requests_list}'
    
def send_chat_notification(message, webhook_url, host_url):
    
    bot_message = {
        'text' : message
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    try:
        while True:
            response = requests.post(url=webhook_url,
                headers=message_headers,
                data=json.dumps(bot_message),
            )
            
            if response.status_code == 200:
                return RedirectResponse(url=host_url)
            
    except Exception as e:
        print(e)