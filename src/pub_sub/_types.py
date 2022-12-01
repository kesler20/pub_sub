from typing import TypedDict, ByteString

class MQTTMessage(TypedDict):
  timestamp: int
  state: bool
  dup: bool
  mid: bool
  topic: str
  payload: ByteString
  qos: int
  retain: bool



