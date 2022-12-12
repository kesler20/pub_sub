import json
import random
import time
from config import *
from src.pub_sub.mqtt_client import MQTTClient
from src.pub_sub._types import MQTTMessage
import datetime
import AWSIoTPythonSDK

# using the epoch time as the x_value which calculates
# the seconds that have passed since 1970
data = 0
x_value = int(datetime.datetime.timestamp(datetime.datetime.now()))
total_1 = 1000
t1s = -6
t1e = 6
trend_1 = 1000

WRITE_TOPIC = 'tff/data'
READ_TOPIC = 'testiot'
MAX_DIAL_INTENSITY = 5

def control_intensity_algorithm(dial_variable):
    return (MAX_DIAL_INTENSITY-dial_variable)/(MAX_DIAL_INTENSITY-1)*14+2


def cb(client: None, user_data: None, message: MQTTMessage) -> None:
    global data
    data = message.payload.decode()
    data = json.loads(data)
    print(data)


client = MQTTClient()
client.subscribe_to_topic(READ_TOPIC, cb)

while True:
    try:
        info = {
            "x_value": data["timestamp"],
            "total_1": data["Value"] + total_1,
            "trend_1": trend_1,
        }

        client.publish_data(WRITE_TOPIC, json.dumps(info))
        print(info)

        trend_1 = trend_1 + (t1e-t1s)/2+t1s

        time.sleep(1)  # in seconds
    except AWSIoTPythonSDK.exception.AWSIoTExceptions.subscribeTimeoutException:
        pass
