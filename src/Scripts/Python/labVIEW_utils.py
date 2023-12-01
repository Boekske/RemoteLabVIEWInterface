import json
import zmq

class RemoteCall:
    """Class for connecting and executing commands over ZeroMQ Using JSON
    """
    socket = 0

    def connect(self,connection_string):
        """ Make the initial connection to the client running in LabVIEW

        Parameters
        ----------
        connection_string : String (Example "tcp://127.0.0.1:5555", "ConnectionType"://"IPAdress":"Port")
        """

        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect(connection_string)

    def execute(self, class_name, method, par_in):
        """ Execute the Method by serializing inputs sending it over, and deserializing the result
        """
        data_2_send = "{ \"Command\":\"Execute\" }\x17{\"ClassLabel\":\"%s\",\"Method\":\"%s\"}\x17%s" % (class_name, method, json.dumps({"In": par_in}))
        self.socket.send_string (data_2_send)
        message = self.socket.recv()
        parts = message.split(chr(0x17).encode())
        return json.loads(parts[1]), json.loads(parts[0])

class LabVIEWerror(Exception):
    """Base class for all LabVIEW errors

    Attributes
    ----------
    code: error code for testing which error happend
    source: source of the error
    """
    def __init__(self, *args: object) -> None:
        self.code = self.args[0]
        self.source = self.args[1]
        super().__init__(*args)

    def __str__(self) -> str:
        return f"LabVIEW Error with code: {self.code} source: {self.source}"
