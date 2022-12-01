import pandas as pd
import unittest
from connector import MQTTClient
import json
from src.pub_sub._types import MQTTMessage
import time

class TestMQTTClient(unittest.TestCase):

    def setUp(self):
        self.test_controller = MQTTClient()
        self.test_device = MQTTClient()
        self.test_read_topic = "test/data"
        self.test_write_topic = "test/control"
        self.message_arrived = ""
        self.test_messages = ["test message", json.dumps({"msg": "test message"}), pd.DataFrame(["test message"]).to_json()]

    def _call_back(self, client: None, user_data: None, message: MQTTMessage):
        self.message_arrived = message.payload.decode()

    def test_run(self):
        """test the workflow of sending data to the broker and reading that data from the script 
        """
        # subscribe device and controller to respective read channels
        self.test_controller.subscribe_to_topic(self.test_read_topic, self._call_back)
        self.test_device.subscribe_to_topic(self.test_write_topic, self._call_back)

        # device publishes data to the AWS broker
        for index, data in enumerate(self.test_messages):
            if index == 0:
                expected_output = "test message"
            elif index == 1:
                expected_output = json.dumps({"msg": "test message"})
            else:
                expected_output = pd.DataFrame(["test message"]).to_json()

            self.test_device.publish_data(self.test_write_topic, data)
            time.sleep(1)
            # controller listens to that data and retrieves the message
            self.assertEqual(self.message_arrived, expected_output)


if __name__ == '__main__':
    unittest.main()
