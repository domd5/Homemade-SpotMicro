from adafruit_servokit import ServoKit
import keyboard

end = True
kit = ServoKit(channels=16)
print("Initializing Servos")

while end:
    text = input()
    if text == 'h':
        print("Standing")
        #top
        kit.servo[0].angle = 90
        kit.servo[3].angle = 90
        kit.servo[6].angle = 90
        kit.servo[9].angle = 90
        #mid
        kit.servo[1].angle = 45
        kit.servo[4].angle = 120
        kit.servo[7].angle = 45
        kit.servo[10].angle = 120
        #bottom
        kit.servo[2].angle = 70
        kit.servo[5].angle = 100
        kit.servo[8].angle = 70
        kit.servo[11].angle = 120
    if text == 't':
        print("Sitting")
        #back
        #top
        kit.servo[6].angle = 90
        kit.servo[9].angle = 90
        #mid
        kit.servo[7].angle = 0
        kit.servo[10].angle = 180
        #bottom
        kit.servo[8].angle = 130
        kit.servo[11].angle = 50
        #front
        #top
        kit.servo[0].angle = 90
        kit.servo[3].angle = 90
        #mid
        kit.servo[1].angle = 75
        kit.servo[4].angle = 90
        #bottom
        kit.servo[2].angle = 0
        kit.servo[5].angle = 180

    if text == 'r':
        print("Laying Down")
        #top
        kit.servo[0].angle = 90
        kit.servo[3].angle = 90
        kit.servo[6].angle = 90
        kit.servo[9].angle = 90
        #mid
        kit.servo[1].angle = 0
        kit.servo[4].angle = 180
        kit.servo[7].angle = 0
        kit.servo[10].angle = 180
        #bottom
        kit.servo[2].angle = 150
        kit.servo[5].angle = 20
        kit.servo[8].angle = 150
        kit.servo[11].angle = 30
    
    if text == 'f':
        print("High Five")
        kit.servo[0].angle = 100
        kit.servo[1].angle = 150
        kit.servo[2].angle = 120
        
        
    if text == 'w':
        print("Disengaging")
        kit.servo[0].angle = None
        kit.servo[1].angle = None
        kit.servo[2].angle = None
        kit.servo[3].angle = None
        kit.servo[4].angle = None
        kit.servo[5].angle = None
        kit.servo[6].angle = None
        kit.servo[7].angle = None
        kit.servo[8].angle = None
        kit.servo[9].angle = None
        kit.servo[10].angle = None
        kit.servo[11].angle = None
        
    if text == 'q':
        print("Ending Program")
        end = False
