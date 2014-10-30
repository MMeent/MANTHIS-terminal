import serial  # download the PySerial library first!
import time


ser = serial.Serial(6, 9600, timeout=1)


if not ser.isOpen():
    ser.open()


def scan(blocknumber):
    ser.write("r".encode())
    ser.write(str(blocknumber).encode())
    ser.write("0000000000000000000000000".encode())
    i = 0
    while ser.inWaiting() < 16:
        i += 1
    data = ser.readline()
    flushall()
    return data.decode()[:16]


def stop():  # use when shuting down connection, otherwise no new one can be set up
    ser.close()
    return "Reading stopped"


def flushall():
    ser.flushInput()
    ser.flushOutput()
    return


def write(blocknumber, data):
    ser.write("w".encode())
    ser.write(str(blocknumber).encode())
    ser.write(data.encode())
    return