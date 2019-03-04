#Date: 20/02/2019
#Author: Nguyen Chi Cuong
#exercise:  Write a python script to read a string "SWI9X15Y_07.11.11.00 r33161 CARMD-EV-FRMWR1 2016/09/20 16:36:44" and parse FW version, date and hour then print them
import re
# define
frameWare = "SWI9X15Y_07.11.11.00"
date = "2016/09/20"
time = "16:36:44"
# function
def readInput():
    print("Input your string please: ")
    while True:
        strInput = input()
        if strInput != "":
            break
        else: print("error, please input again:\n")
    return strInput
#############
def search1(input, Fw, date, time):
    if(re.findall(Fw, input)): 
        print("Fw: SWI9X15Y_07.11.11.00")
    if(re.findall(date, input)): 
        print("date: 2016/09/20")
    if(re.findall(time, input)): 
        print("time: 16:36:44")
    else: pint("no match")
############
def search2(input, keywork):
    search = re.search(keywork, input)
    print(search.group())
def filter(input):
    print("FW: " + input[0:20])
    print("Date: " + input[44:54])
    print("Time: " + input[55:64])

# MAIN #######
inp = readInput().strip()
search1(inp,"SWI9X15Y_07.11.11.00", "2016/09/20", "16:36:44")    
print("search 2________________________________________________")
search2(inp, frameWare)
search2(inp, date)
search2(inp, time)
print("filter _________________________________________________")
filter(inp)