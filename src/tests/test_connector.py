import pandas as pd
import unittest
from connector import MQTTClient
import json


class Test_MQTTClient(unittest.TestCase):

    def setUp(self):
        self.test_client = MQTTClient()
        self.test_topic = "test/data"
        self.test_messages = ["test message", json.dumps({"msg": "test message"}), pd.DataFrame(["test message"]).to_json()]

    def _call_back(self, client, user_data, message):
        self.message = message

    def test_io_publish_data(self):
        """
        test the publish_data method which accepts the following arguments:

        Params:
        ---
        topic: str, payload: str, quos: Optional[int] = 0

        Returns:
        ---
        -  None
        """
        # array of arguments which are expected by the method being tested
        correct_inputs = [*self.test_messages]
        # array containing the expected correct result of the function call
        correct_output = [None]

        # array of arguments containing an invalid type
        invalid_types_inputs = [*self.test_messages, pd.DataFrame(["test message"])]
        # array containing the result of the function call
        invalid_types_output = [None]

        # array of arguments containing an invalid value
        invalid_values_inputs = [*self.test_messages, ""]
        # array containing the result of the function call
        invalid_values_output = [None]

        for message in correct_inputs:
            test_result = self.test_client.publish_data(self.test_topic, message)
            self.assertEqual(test_result, correct_output[0])
            # assert that the type returned by the method is correct
            self.assertEqual(type(test_result), type(None))

        for invalid_types_message in invalid_types_inputs:
            test_result = self.test_client.publish_data(self.test_topic, invalid_types_message)
            self.assertEqual(test_result, invalid_types_output[0])
            # assert that the type returned by the method is correct
            self.assertEqual(type(test_result), type(None))

        for invalid_values_message in invalid_values_inputs:
            test_result = self.test_client.publish_data(self.test_topic, invalid_values_message)
            self.assertEqual(test_result, invalid_values_output[0])
            # assert that the type returned by the method is correct
            self.assertEqual(type(test_result), type(None))

    def test_io_subscribe_to_topic(self):
        """
        test the subscribe_to_topic method which accepts the following arguments:

        ---
        Params:
        topic: str, custom_callback, quos: Optional[int] = 1

        ---
        Returns:
        -  None
        """
        # array of arguments which are expected by the method being tested
        correct_input = [self.test_topic,self._call_back]
        # array containing the expected correct result of the function call
        correct_output = [None]

        # array of arguments containing an invalid type
        invalid_types_input = [self.test_topic, 1]
        # array containing the result of the function call
        invalid_types_output = [None]

        # array of arguments containing an invalid value
        invalid_values_input = [self.test_topic, ""]
        # array containing the result of the function call
        invalid_values_output = [None]

        test_result = self.test_client.subscribe_to_topic(*correct_input)
        self.assertEqual(test_result, correct_output[0])

        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result), type(None))

        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result), type(None))

        test_result = self.test_client.subscribe_to_topic(*invalid_types_input)
        self.assertEqual(test_result, invalid_types_output[0])

        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result), type(None))

        test_result = self.test_client.subscribe_to_topic(*invalid_values_input)
        self.assertEqual(test_result, invalid_values_output[0])

        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result), type(None))

    def tearDown(self) -> None:
        self.test_client.tear_down(self.test_topic)
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
