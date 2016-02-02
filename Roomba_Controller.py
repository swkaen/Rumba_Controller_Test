# -*- coding: utf-8 -*-
import serial
import time

def sendCommandASCII(self, command):
    cmd = ""
    for v in command.split():
        cmd += chr(int(v))

    self.sendCommandRaw(cmd)

def sendCommandRaw(self, command):
    connection.write(command)
                
if __name__ == "__main__":
	connection = serial.Serial('/dev/tty.usbserial-DA017LBH', baudrate=115200, timeout=1)
	connection.write(bytes([143]))

