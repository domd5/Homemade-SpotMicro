from adafruit_servokit import ServoKit
import keyboard
import time

end = True
kit = ServoKit(channels=16)
print("Initializing Servos")

# Helper: move one leg through a step cycle
def step_leg(kit, top, mid, bot, top_stand, mid_stand, bot_stand, forward=True):
    swing_angle = top_stand + (15 if forward else -15)
    
    # Lift
    kit.servo[mid].angle = mid_stand - 20  # raise thigh
    time.sleep(0.15)
    
    # Swing forward
    kit.servo[top].angle = swing_angle
    time.sleep(0.15)
    
    # Plant
    kit.servo[mid].angle = mid_stand
    kit.servo[bot].angle = bot_stand
    time.sleep(0.15)

while end:
    text = input()
    if text == 'e':
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
    if text == 'z':
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
        
    #if text == 'w':
        #print("Walking")
        #text = e 
        #fl
        #kit.servo[3].angle = 90
        #kit.servo[4].angle = 45
        #kit.servo[5].angle = 70
        #br
        #kit.servo[6].angle = 90
        #kit.servo[7].angle = 0
        #kit.servo[8].angle = 130

    if text == 'a':
        print("Walking Forward")
        # Standing angles from your 'h' command:
        # FL: top=0,mid=1,bot=2  |  FR: top=3,mid=4,bot=5
        # BL: top=6,mid=7,bot=8  |  BR: top=9,mid=10,bot=11

        for _ in range(4):  # 4 step cycles
            step_leg(kit, 0, 1, 2,  90, 45, 70, False)   # Front-Left
            step_leg(kit, 9, 10, 11, 90, 120, 120) # Back-Right
            step_leg(kit, 3, 4, 5,  90, 120, 100)  # Front-Right
            step_leg(kit, 6, 7, 8,  90, 45, 70, False)    # Back-Left

        
    if text == '1':
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
