import random

while(1):

    temp=random.randint(0,100)

    humid=random.randint(0,100)

    print("temperature level:"+str(temp))

    print("humidity level:"+str(humid))

    if(temp==range(27,38) and humid==range(30,50)):       

        print("NORMAL TEMPERATURE")

    elif(temp<27 or humid>50):

        print("COOL TEMPERATURE")

    elif(temp>38 or humid<30):

        print("ALERT -VERY HIGH TEMPERATURE")
