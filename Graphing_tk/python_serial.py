import serial
import matplotlib.pyplot as plt
from drawnow import *

values = []
plt.ion()
cnt = 0

serialArduino = serial.Serial('COM4', 9600)


def plotValues():
    plt.title('Serial value from Arduino')
    plt.xlim(0,100)
    plt.ylim(0,1000)
    plt.ylabel('Pressure')
    plt.plot(values,label='Pressure')
    plt.legend(loc='upper right')

# pre-load dummy data
for i in range(0, 100):
    values.append(0)


for i in range(0, 100):
    #while (serialArduino.inWaiting() == 0):
        #pass
    valueRead = serialArduino.readline()
    valueInInt = int(valueRead)
    print(valueInInt)
    if valueInInt <= 1024:
        if valueInInt >= 0:
            values.append(valueInInt)
            values.pop(0)
            drawnow(plotValues)





