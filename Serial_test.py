# -*- coding: utf-8 -*-
import serial
connection = serial.Serial("/dev/tty.SLAB_USBtoUART", baudrate=9600)
while True:
    print(connection.read())