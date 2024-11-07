from enum import Enum
from typing import Dict
from dataclasses import dataclass


class StateType(Enum):
    MAIN = 1
    SEARCH = 2


@dataclass
class State:
    type: StateType
    data: any


state: dict[int, State] = {}


def get(peer_id: int) -> State:
    if peer_id not in state:
        set(peer_id, State(StateType.MAIN, None))
    return state[peer_id]


def set(peer_id: int, data: State):
    state[peer_id] = data


def delete(peer_id: int):
    state.pop(peer_id)



