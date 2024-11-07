import methods
import keyboard
from handlers import handle_new_message, handle_event_message
from vk import vk
import config
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


longpoll = VkBotLongPoll(vk, group_id=config.group_id)


while True:
    events = longpoll.check()
    for event in events:
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            handle_new_message(event)
        if event.type == VkBotEventType.MESSAGE_EVENT:
            handle_event_message(event)
