from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol
from enum import Enum, auto
from pydantic import BaseModel, validator


class QualityofService(Enum):
    AT_MOST_ONCE = 0
    AT_LEAST_ONCE = 1
    EXACTLY_ONCE = 2


@dataclass
class MQTTMessage(BaseModel):
    timestamp: int
    state: bool
    dup: bool
    mid: bool
    topic: str
    payload: bytes
    qos: QualityofService
    retain: bool

    @validator('payload')
    def payload_not_exceeding_limit(cls, payload):
        if len(payload) >= 256000000:
            raise ValueError


class HeartBitPackage:
    """2bytes package to check that the equipment is not down"""
    pass


class MQTTProtocol(Protocol):

    def birth_message(self) -> str:
        ...

    def death_message(self) -> str:
        ...

    def last_will_and_testament(self) -> str:
        ...

    def keep_alive_timer(self) -> int:
        ...

    def disconnect_client(self) -> bool:
        ...

    def connected(self) -> bool:
        ...

    def connect_client(self) -> None:
        ...

    def port(self) -> int:
        ...


class MQTTSessionState(Enum):
    CONNECTION = auto()
    AUTHENTICATION = auto()
    COMMUNICATION = auto()
    TERMINATION = auto()
    
# implement the state pattern on the MQTTSession


class MQTTSession(ABC):

    _state: MQTTSessionState
