from typing import TypedDict


class MQTTMessage(TypedDict):
  timestamp: int
  state: bool
  dup: bool
  mid: bool
  topic: str
  payload: None
  qos: int
  retain: bool



