import vk_api
import random
from vk import vk


def write_msg(user_id, message, key):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'keyboard': key,
               'random_id': random.randint(0, 2048)})
