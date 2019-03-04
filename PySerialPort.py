import serial, time
port = "COM8"
cmdCheckImei = ["AT", "AT+GSN=?", "AT+GSN"]
cmdCheckService = ["AT","AT+COPS?", "AT+COPS"]
def openPort(port):

    try:
        ser = serial.Serial(port)
        print("Port " + port + " is opened successfull")
        return ser
    except serial.SerialException:
        print("Port " + port + " is opened before")
        return None
def closePort(ser):
    ser.close()
    print("closed port " , ser.port)
def sendATCommands(commands, ser):
    for cmd in commands:
        strCmd = cmd + '\r\n'
        ser.write (strCmd.encode())
        time.sleep(0.1)
        if ser.inWaiting() > 0:
            bytesNum = ser.inWaiting()
            result = ser.read(bytesNum)
            print(result)
# Main ######
ser = openPort(port)  
if ser:
    sendATCommands(cmdCheckImei, ser)
    sendATCommands(cmdCheckService, ser)
    closePort(ser)