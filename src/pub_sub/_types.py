from dataclasses import dataclass


@dataclass
class MQTTMessage:
    timestamp: int
    state: bool
    dup: bool
    mid: bool
    topic: str
    payload: bytes
    qos: int
    retain: bool
