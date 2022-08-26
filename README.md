# Radio Spare Pro Programmable Power Supply IPS603 controler over RS232

Python controler to drive a Radio Spare Programmable Power Supply IPS603 with RS232 connexion

Installation
```
python3 -m pip install -r requirements.txt
```

Quick Start
```
python3 main.py --serial /dev/ttyUSB0
```

don't forget to `sudo chmod 666 /dev/ttyUSB0` if you have the following error `Permission denied: '/dev/ttyUSB0'`

source: https://docs.rs-online.com/d6a8/0900766b80269a3a.pdf
