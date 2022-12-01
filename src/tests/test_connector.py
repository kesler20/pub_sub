import pandas as pd
import unittest
from connector import MQTTClient
import json    

class Test_MQTTClient(unittest.TestCase):

  def setUp(self):
    self.test_client = MQTTClient()
    self.test_topics = ["test/data","test/control"]
    self.test_messages = ["test message", json.dumps({ "msg" : "test message" }), pd.DataFrame(["test message"]).to_json()]

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
    correct_input = [*self.test_messages]
    # array containing the expected correct result of the function call
    correct_output = [None]

    # array of arguments containing an invalid type 
    invalid_types_input = [*self.test_messages, pd.DataFrame(["test message"])]
    # array containing the result of the function call
    invalid_types_output = [None]

    # array of arguments containing an invalid value 
    invalid_values_input = [*self.test_messages,""]
    # array containing the result of the function call
    invalid_values_output = [None]

    test_result = self.test_client.publish_data(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None)) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None))

    test_result = self.test_client.publish_data(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None))

    test_result = self.test_client.publish_data(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None))

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
    correct_input = [*self.test_topics]
    # array containing the expected correct result of the function call
    correct_output = [None]

    # array of arguments containing an invalid type 
    invalid_types_input = [*self.test_topics, 1]
    # array containing the result of the function call
    invalid_types_output = [None]

    # array of arguments containing an invalid value 
    invalid_values_input = [*self.test_topics, ""]
    # array containing the result of the function call
    invalid_values_output = [None]

    test_result = self.test_client.subscribe_to_topic(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None)) 

    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None))

    test_result = self.test_client.subscribe_to_topic(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type(None))

    test_result = self.test_client.subscribe_to_topic(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))
  
  def tearDown(self) -> None:
    self.test_client.tear_down(*self.test_topics)
    return super().tearDown()


if __name__ == '__main__':
    unittest.main()