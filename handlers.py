import keyboard
import methods
import state
from state import StateType, State


welcome_message = "Выберите нужное на клавиатуре под полем ввода текста"


def handle_new_message(event):
    peer_id = event.obj['message']['peer_id']
    text = event.obj['message']['text']
    payload = event.obj['message']['payload'] if 'payload' in event.obj['message'] else None

    if payload == "{\"command\":\"start\"}":
        start(peer_id)

    match state.get(peer_id).type:
        case StateType.MAIN:
            if methods.compare_input(text, "поиск"):
                begin_searching(peer_id)
            else:
                start(peer_id)
        case StateType.SEARCH:
            if methods.compare_input(text, "отменить"):
                start(peer_id)
            else:
                search(peer_id, text)


def handle_event_message(event):
    peer_id = event.obj['peer_id']
    message_id = event.obj['conversation_message_id']
    payload = event.obj['payload']


def begin_searching(peer_id):
    state.set(peer_id, State(StateType.SEARCH, None))
    methods.write_msg(peer_id, "Введите название места", keyboard.searching)


def search(peer_id, text):
    state.set(peer_id, State(StateType.MAIN, None))
    methods.write_msg(peer_id, f"По запросу {text} ничего не нашлось", None)  # TODO


def start(peer_id):
    state.set(peer_id, State(StateType.MAIN, None))
    methods.write_msg(peer_id, welcome_message, keyboard.main_keyboard)
