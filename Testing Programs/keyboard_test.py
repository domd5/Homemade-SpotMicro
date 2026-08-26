import keyboard  # pip3 install keyboard
repeat=0

while repeat < 2:
    if keyboard.is_pressed('space'):
        print("Space is held down")
        repeat +=1
        break

    if keyboard.is_pressed('f'):
        print("f is held down")
        repeat +=1
        break

