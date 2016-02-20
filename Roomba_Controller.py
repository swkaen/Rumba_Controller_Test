# -*- coding: utf-8 -*-
import serial
import time
import struct
from websocket import create_connection



connection = None
VELOCITY_CHANGE = 200
ROTATION_CHANGE = 300

callbackLeverUp    = False
callbackLeverDown  = False
callbackLeverLeft  = False
callbackLeverRight = False
callbackLeverLastDriveCommand = ''

def onConnect(serial_port):
    global connection
    connection = serial.Serial(serial_port, baudrate=115200, timeout=1)

def sendCommandRaw(command):
    connection.write(command)

def callBackKey(event):

    velocity = 0
    velocity += VELOCITY_CHANGE if callbackLeverUp is True else 0
    velocity -= VELOCITY_CHANGE if callbackLeverDown is True else 0
    rotation = 0
    rotation += ROTATION_CHANGE if callbackLeverLeft is True else 0
    rotation -= ROTATION_CHANGE if callbackLeverRight is True else 0

    vr = velocity + (rotation/2)
    vl = velocity - (rotation/2)
    cmd = struct.pack(">Bhh", 145, vr, vl)

    sendCommandRaw(cmd)

if __name__ == "__main__":
    ws = create_connection("ws://133.2.37.129:52020/websocket")
    connection = serial.Serial('/dev/tty.usbserial-DA017LBH', baudrate=115200, timeout=1)
    while True:
        #print("-"*10 + 'choose command'+ "-"*10)
        #print("c:Clrean, p:Passive, s:Safe, d:Dock")
        #print("i:go, k:back, l:turn right, j:turn left")
        #print('command:', end="")
        #cmd = input()
        cmd  = ws.recv()
        print(cmd)
        if cmd == "c": 
            connection.write(bytes([135]))
        elif cmd == 'p':
            connection.write(bytes([128]))
        elif cmd == 's':
            connection.write(bytes([131]))
        elif cmd == 'd':
            connection.write(bytes([143]))
        elif cmd == 'i':
            command = struct.pack(">Bhh", 145, 200, 200)
            connection.write(command)
        elif cmd == 'k':
            command = struct.pack(">Bhh", 145, -200, -200)
            connection.write(command)
        elif cmd == 'l':
            command = struct.pack(">Bhh", 145, -200, 200)
            connection.write(command)
        elif cmd == 'j':
            command = struct.pack(">Bhh", 145, 200, -200)
            connection.write(command)
        elif cmd == 'song':
            connection.write(bytes([140,3,10,72,16,141,3]))



