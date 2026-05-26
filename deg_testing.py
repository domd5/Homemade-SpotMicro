from adafruit_servokit import ServoKit

end = True
kit = ServoKit(channels=16)
print("Initializing Servos")

while end:
    port = input("Servo Port")
    deg = input("Degree")
    if port == 'q':
        print("Ending Program")
        end = False
    kit.servo[int(port)].angle = int(deg)
