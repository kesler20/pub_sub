import string
import random
from typing import Callable, Optional, Any, List, Tuple
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from config import END_POINT, PATH_TO_ROOT_CA, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE
from src.pub_sub._types import MQTTMessage


class MQTTClient:
    """AWS IoT MQTT Clients using TLSv1.2 Mutual Authentication
    for more information on AWS documentation see 
    https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/html/index.html#module-AWSIoTPythonSDK.MQTTLib

    to implement the client you can subscribe to a channel and 
    implement some logic within a loop i.e.:

    ```python   
    def cb(client: None,user_data: None,message: MQTTMessage) -> None:
        data = message.payload.decode()
        print(data)

    client = MQTTClient() 
    client.subscribe_to_topic("device/control",cb)
    flag = 0
    while True:
        try:
            # application running in the loop
            if flag:
                client.publish_data("device/data","hello world")
            ...
        except AWSIoTPythonSDK.exception.AWSIoTExceptions.subscribeTimeoutException:
            pass
    ```

    The client is connected when the constructor is called, and can be disconnected using the tear_down method
    """

    def __init__(self) -> None:
        self._clientID = self._generate_clientID()
        self._client: AWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(self._clientID)
        self._connect_client()

    @property
    def clientID(self) -> str:
        """returns a random string of 8 digits"""
        return self._clientID

    def _generate_clientID(self, length: int = 8) -> str:
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def _connect_client(self) -> None:
        self._client.configureEndpoint(END_POINT, 8883)
        self._client.configureCredentials(
            PATH_TO_ROOT_CA, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)
        self._client.connect(keepAliveIntervalSecond=900)

    def _guard_clause(self, args: List[Tuple[Any, Any]], result) -> Any:
        """Every public method should call the guard clause"""
        if False in [type(var) == var_type for var, var_type in args]:
            return result
        else:
            return "guarded"

    def tear_down(self, *topics) -> None:
        for topic in topics:
            self._client.unsubscribe(topic)
        self._client.disconnect()

    def publish_data(self, topic: str, payload: str, quos: Optional[int] = 0) -> Any:
        """publish to the given topic

        Params
        ---
        topic: str
            the topic which the client listens too
        payload: str
            the payload which will be sent
        quos: int
            Quality of Service set to 0 (at most once) as default

        Returns
        ---
        None 

        Note
        ---
        if you want to pass a dictionary as payload

        ```python
        import json

        json.dumps(my_dict)
        ```
        if you want to pass a pandas data frame

        ```python
        import pandas as pd
        df = pd.DataFrame([1,2])
        df.to_json()
        ```
        """

        if self._guard_clause([(topic, str), (payload, str)], None) is None:
            return None
        return None if self._client.publish(topic, payload, quos) else False

    def subscribe_to_topic(self, topic: str, custom_callback: Callable[[None, None, MQTTMessage], None], quos: Optional[int] = 1) -> Any:
        """subscribe to the given topic

        Params
        ---
        topic: str 
            the topic which the client listens too
        custom_callback: func
            the function which will be called anytime a new message arrives
        quos: int
            Quality of Service set to 1 (At least once) as default

        Returns
        ---
        None 

        Note
        ---
        Callback functions should be of the following form:
        ```python
        def callback(client: None,used_data: None ,message: MQTTMessage) -> None:
            function(message)
        ```
        where message has properties message.payload and message.topic"""

        if self._guard_clause([(topic, str)], None) is None:
            return None
        return None if self._client.subscribe(topic, quos, custom_callback) else False


