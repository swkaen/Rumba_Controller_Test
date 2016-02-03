# -*- coding: utf-8 -*-
import serial
import time

connection = None

def onConnect(serial_port):
    global connection
    connection = serial.Serial(serial_port, baudrate=115200, timeout=1)

def sendCommandRaw(command):
    connection.write(command)
                
if __name__ == "__main__":
    connection = serial.Serial('/dev/tty.usbserial-DA017LBH', baudrate=115200, timeout=1)
    connection.write(bytes([143]))
    connection.write(bytes([135]))
    
