from adafruit_servokit import ServoKit
import keyboard

end = True
kit = ServoKit(channels=16)
print("Initializing Servos")

while end:
    text = input()
    if text == 'f':
        print("Testing Sholders")
        kit.servo[0].angle = 90
        kit.servo[3].angle = 90
        kit.servo[6].angle = 90
        kit.servo[9].angle = 90
    if text == 'g':
        print("Single Leg Standing")
        kit.servo[3].angle = 90
        kit.servo[4].angle = 120
        kit.servo[5].angle = 10
    if text == 'b':
        print("single leg stand other side")
        kit.servo[0].angle = 90
        kit.servo[1].angle = 45
        kit.servo[2].angle = 180
    if text == 'h':
        print("All Legs Stand")
        #front
        kit.servo[0].angle = 90
        kit.servo[1].angle = 45
        kit.servo[2].angle = 70
        kit.servo[3].angle = 90
        kit.servo[4].angle = 120
        kit.servo[5].angle = 100
        #back
        kit.servo[6].angle = 90
        kit.servo[7].angle = 45
        kit.servo[8].angle = 70
        kit.servo[9].angle = 90
        kit.servo[10].angle = 120
        kit.servo[11].angle = 120
    if text == 't':
        print("Sitting")
         #front
        kit.servo[0].angle = 90
        kit.servo[1].angle = 75
        kit.servo[2].angle = 0
        kit.servo[3].angle = 90
        kit.servo[4].angle = 90
        kit.servo[5].angle = 180
        #back
        kit.servo[6].angle = 90
        kit.servo[7].angle = 0
        kit.servo[8].angle = 130
        kit.servo[9].angle = 90
        kit.servo[10].angle = 180
        kit.servo[11].angle = 50
    if text == 'r':
        print("Laying Down")
         #front
        kit.servo[0].angle = 90
        kit.servo[1].angle = 0
        kit.servo[2].angle = 150
        kit.servo[3].angle = 90
        kit.servo[4].angle = 180
        kit.servo[5].angle = 20
        #back
        kit.servo[6].angle = 90
        kit.servo[7].angle = 0
        kit.servo[8].angle = 150
        kit.servo[9].angle = 90
        kit.servo[10].angle = 180
        kit.servo[11].angle = 30
        
    if text == 'q':
        print("Ending Program")
        end = False
