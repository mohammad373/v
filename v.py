# v

import os
import sys
import time
import socket

def __1__():
    time.sleep(1)
    print("Hello . Welcome Back ;)")
    time.sleep(1)
    target = input("Pleass Enter Your Address Target ==>  ")
    if target == "" or None :
        try:
            time.sleep(1)
            print("Error : Your Target Is Not Found Or None ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if not "https" in target or not "http" in target :
        target = "http://" + target
    my_list = []
    print("\n")
    time.sleep(1)
    while True:
        time.sleep(0.2)
        q = input("Pleass Enter Your List ==>  ")
        my_list.append(q)
        if q == "exit" or q == "" or q == None  or q == "666":
            break
    for i in my_list:
        host = target + "/" + i
        bypass = socket.gethostbyname(host)
        if bypass_status_code == 200:
            print("This Is Ok ;) + Your Ip ==>  " + host + bypass)
        else:
            print("This Is Not Ok ;( " + host)
__1__()

