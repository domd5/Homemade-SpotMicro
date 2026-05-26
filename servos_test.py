from adafruit_servokit import ServoKit
import time
print("Initializing Servos")
kit = ServoKit(channels=16)
repeat = 0
while repeat < 1:
    print("move top")
    kit.servo[0].angle = 90
    time.sleep(1)

    kit.servo[0].angle = 0
    time.sleep(1)
    #print("move mid")
    #kit.servo[1].angle = 90
    #time.sleep(1)

    #kit.servo[1].angle = 0
    #time.sleep(1)
    #print("move bottom")
    #kit.servo[2].angle = 90
    #time.sleep(1)

    #kit.servo[2].angle = 0
    #time.sleep(1)
    
    kit.servo[3].angle = 90
    #kit.servo[4].angle = 0
    #kit.servo[5].angle = 0
    kit.servo[6].angle = 90
    #kit.servo[7].angle = 0
    #kit.servo[8].angle = 0
    kit.servo[9].angle = 90
    #kit.servo[10].angle = 0
    #kit.servo[11].angle = 0
    
    repeat += 1
    print("done",repeat, "time")
