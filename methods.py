import vk_api
import random
from vk import vk
from cleantext import clean


def write_msg(user_id, message, key):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'keyboard': key,
               'random_id': random.randint(0, 2048)})


def compare_input(input_str: str, phrase: str):
    input_str = clean(input_str, lower=True, no_emoji=True)
    phrase = clean(phrase, lower=True)
    return input_str == phrase
