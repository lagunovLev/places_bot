import methods
from vk import vk
import config
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


longpoll = VkBotLongPoll(vk, group_id=config.group_id)


while True:
    events = longpoll.check()
    for event in events:
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj['message']['peer_id']
            text = event.obj['message']['text']
            methods.write_msg(user_id, text, None)
