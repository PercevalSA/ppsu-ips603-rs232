# source: https://docs.rs-online.com/d6a8/0900766b80269a3a.pdf

import serial


class IPS603:
    def __init__(self, serialport="/dev/ttyUSB0"):
        """connect to serial interface to send commands to PPSU

        Args:
            serial (_type_): _description_
        """
        print("Opening Serial Communication")
        BAUDRATE = 2400
        self.serial_con = serial.Serial(serialport, BAUDRATE, timeout=1)

    def _send(self, command: str) -> str:
        """send command on serial port

        Args:
            command (str or bytes): command to send to the PPSU

        Returns:
            str: response from PPSU
        """

        # to handle both str and bytesq like 'L\n' or b'\x4C\x0D'
        if isinstance(command, str):
            command = command.encode()

        ret = self.serial_con.write(command)
        print(f"write: {ret}")

        response = self.serial_con.readline()
        print(f"Reading: {response}")
        # print(f"UTF-8: {response.decode('utf-8')}")

        self.serial_con.flush()  # flush the buffer
        return response

    def getValues(self):
        response = self._send("L\n")  # b'\x4C\x0D'
        print(f"Values: {response}")

    def getTension(self):
        self._send("V\r")

    def getIntensity(self):
        self._send("A\n")

    def getPower(self):
        self._send("W\n")

    def getMaxTension(self):
        self._send("U\n")

    def getMaxIntensity(self):
        self._send("I\n")

    def getMaxPower(self):
        self._send("P\n")

    def getStatus(self):
        response = self._send("F\n")
        print(f"Status: {response}")  # 7 chars
