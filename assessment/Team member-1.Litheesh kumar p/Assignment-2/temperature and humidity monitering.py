

import random
import sys
from time import sleep
class smartmonitor():
    def func(self):
        temp=random.randint(0,100)
        humid=random.randint(0,100)
        print("temperature level:"+str(temp))
        print("humidity level:"+str(humid))
        if(temp==range(27,38) and humid==range(30,50)):        print("no problem-->its a normal condition")
        elif(temp<27 or humid>50):
            print("now you are in cool mode please wear the sweater")
        elif(temp>38 or humid<30):
            print("fire accident is happening immediate action needs to be taken")
    def func1(self):
        try:
            while(1):
                self.func()
                sleep(1)
        except KeyboardInterrupt:
            print()
            print("Do you want to exit:y/n")
            st=input()
            if(st=='y'):
                sys.exit(0)
            else:
                self.func1()
    def __init__(self):
        self.func1()
smartmonitor()
