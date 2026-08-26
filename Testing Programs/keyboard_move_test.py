from adafruit_servokit import ServoKit
import keyboard

end = True
kit = ServoKit(channels=16)
print("Initializing Servos")

while end:
    if keyboard.is_pressed('f'):
        print("Testing Sholders")
        kit.servo[0].angle = 90
        kit.servo[3].angle = 90
        kit.servo[6].angle = 90
        kit.servo[9].angle = 90
    if keyboard.is_pressed('g'):
        print("Single Leg Standing")
        kit.servo[3].angle = 90
        kit.servo[4].angle = 120
        kit.servo[5].angle = 10
    if keyboard.is_pressed('b'):
        print("single leg stand other side")
        kit.servo[0].angle = 90
        kit.servo[1].angle = 45
        kit.servo[2].angle = 155
    if keyboard.is_pressed('h'):
        print("All Legs Stand")
        #front
        kit.servo[0].angle = 90
        kit.servo[1].angle = 120
        kit.servo[2].angle = 10
        kit.servo[3].angle = 90
        kit.servo[4].angle = 120
        kit.servo[5].angle = 10
        #back
        kit.servo[6].angle = 90
        kit.servo[7].angle = 120
        kit.servo[8].angle = 10
        kit.servo[9].angle = 90
        kit.servo[10].angle = 120
        kit.servo[11].angle = 10

    if keyboard.is_pressed('esc'):
        print("Ending Program")
        end = False
