import serial, time, re
import logging

cmdCheckImei = ["AT", "AT+GSN=?", "AT+GSN"]
cmdCheckService = ["AT","AT+COPS?", "AT+COPS"]
checkAT = ["AT"]
disableEcho = ["ATE1"]
setBauldRate = ["AT+IPR=?", "AT+IPR?", "AT+IPR = 9600"]
revistionIdentifi = ["AT+CGMR=?", "AT+CGMR"]
enterPin = ["AT+CPIN=?", "AT+CPIN?", "AT+CPIN = 3699"]
operator = ["AT+COPS=?", "AT+COPS = 2", "AT+COPS = 0"]
phoneFunctions = ["AT+CFUN = 4"]
checkNetwork = ["AT+CREG?"]
resetModule = ["AT+CFUN = 1,1"]
def COMinput():
    print("please, input your port COM : ")
    while True:
        strInput = input()
        if re.findall("^COM\d", strInput) :
            break
        else: print("error, please input again:\n")
    return strInput
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
        strCmd = cmd  + '\r'
        logging.info(strCmd)
        ser.write (strCmd.encode())
        if(cmd == "AT+COPS=?"):
            time.sleep(60)
        else:
            time.sleep(1)
        if ser.inWaiting() > 0:
            bytesNum = ser.inWaiting()
            result = ser.read(bytesNum)
            format1 = str(result, 'utf-8').replace('\r','')
            format2 = format1.replace('\n','')
            logging.info(format2)
            if len(re.findall("ERROR", str(result, 'utf-8'))) > 0 or not str(result, 'utf-8') :
                print("FAILED")
                logging.info("FAILED\n" + "-" * 50)
            else:
                print("PASSED")
                logging.info("PASSED\n" + "-" * 50)
                # if re.findall("2)", format2):
                #     print("co' 3G nha")

# Main #####
open('logTime.log', 'w+').close()
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S ', filename='logTime.log',level=logging.DEBUG)
logging.info("start\n" + "-" * 50)
ser = openPort(COMinput())  
if ser:
    sendATCommands(checkAT, ser)
    sendATCommands(disableEcho, ser)
    sendATCommands(setBauldRate, ser)
    sendATCommands(revistionIdentifi, ser)
    sendATCommands(enterPin, ser)
    sendATCommands(cmdCheckImei, ser)
    sendATCommands(cmdCheckService, ser)
    sendATCommands(operator, ser)
    sendATCommands(phoneFunctions, ser)
    sendATCommands(checkNetwork, ser)
    sendATCommands(resetModule, ser)
    closePort(ser)
logging.info("finish\n" + "-" * 50)