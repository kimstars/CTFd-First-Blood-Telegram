

import requests
import time

import config
import json

def send_telegram_message(token=config.TELE_TOKEN, chat_id=config.CHAT_ID, message=""):
    print("message: ", message)
    try:
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
        response = requests.get(url)
        print(response.text)
        return response
    except Exception as e:
        print("Error send message telegram: ", e)
        return None
    

class Announcer:
    solve_string: str
    first_blood_string: str
    rate_limit_remaining: int
    rate_limit_sleep_time: int

    def __init__(self):
      
        self.solve_string = config.SOLVE_ANNOUNCE_STRING
        self.first_blood_string = config.FIRST_BLOOD_ANNOUNCE_STRING
        self.rate_limit_remaining = 1
        self.rate_limit_sleep_time = 0

    async def announce(self,
                 chal_name: str,
                 user_name: str,
                 emoji: str,
                 first_blood: bool = False):

        message_send = ""
        print("call annoe")
        if first_blood:
                message_send = self.first_blood_string.format(user_name=user_name,
                                            chal_name=chal_name,
                                            emojis=emoji)
        else:
            message_send = self.solve_string.format(user_name=user_name,
                                        chal_name=chal_name,
                                        emojis=emoji)
        
        send_telegram_message(message=message_send)
        
# message_send = "🔪🩸 Hiểu *First Blood* là gì chưa các bạn!"
# send_telegram_message(message=message_send)