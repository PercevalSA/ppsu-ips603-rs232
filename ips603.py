# source: https://docs.rs-online.com/d6a8/0900766b80269a3a.pdf

import serial

class IPS603:

    def __init__(self, serialport = "/dev/ttyUSB0"):
        """connect to serial interface to send commands to PPSU

        Args:
            serial (_type_): _description_
        """
        print("Opening Serial Communication")
        BAUDRATE = 2400
        self.serial_con = serial.Serial(serialport, BAUDRATE, timeout=2)

    def _send(self, command: str) -> str:
        """send command on serial port

        Args:
            command (str): command to send to the PPSU

        Returns:
            str: response from PPSU
        """
        self.serial_con.write(command.encode())
        response = self.serial_con.readline() 

        # print(f"Reading: {response}") 
        # readOut = ser.readline().decode('ascii')
        # self.serial_con.flush() #flush the buffer

        return response

    def getValues(self):
        self._send("L\n")
        print(f"Values : {response}")

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
        self._send("F\n")
        # 7 chars
