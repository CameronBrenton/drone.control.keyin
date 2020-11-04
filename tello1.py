import tello_abridged
t = tello_abridged.Tello()
t.connect_and_initialize()
#connects the drone to your wifi and enters control mode
while True:
    
    x = str(input("Input a command: "))
# the program will contunually prompt for inputs to contol the drone in real time
    
    if x.lower() == "takeoff":
        t.send_command("takeoff")
#instructs the drone to take off  
    
    if x.lower() == "up":
        y = int(input("How many centimetres would you like to move up? (20 - 500cm): "))
        if (y > 20) and (y < 500):
            t.send_command("up {}".format(y))
        else:
            print("out of range, try again!(20 - 500)")
#instructs the drone to fly up a specified ammout of cm between 20 and 500
    
    if x.lower() == "down":
        y = int(input("How many centimetres would you like to move down? (20 - 500cm): "))
        if (y > 20) and (y < 500):
            t.send_command("down {}".format(y))
        else:
            print("out of range, try again!(20 - 500)")
            continue
#instructs the drone to fly down a spcified ammount of cm between 20 and 500

    if x.lower() == "left":
        y = int(input("How many centimetres would you like to move left? (20 - 500cm): "))
        if (y > 20) and (y < 500):
            t.send_command("left {}".format(y))
        else:
            print("out of range, try again!(20 - 500)")
#instructs the drone to move to the left by a specified ammount of cm between 20 and 500
    
    if x.lower() == "right":
        y = int(input("How many centimetres would you like to move right? (20 - 500cm): "))
        if (y > 20) and (y < 500):
            t.send_command("right {}".format(y))
        else:
            print("out of range, try again!(20 - 500)")
#instructs the drone to move to the right by a specified ammount of cm between 20 and 500
   
    if x.lower() == "forward":
        y = int(input("How many centimetres would you like to move forward? (20 - 500cm): "))
        if y > 20 and y < 500:
            t.send_command("forward {}".format(y))
        else:
            print("Out of range, try again!(20 - 500) ")
            continue
#instructs the drone to fly forward a specified ammount of cm between 20 and 500
    
    if x.lower() == "back":
        y = int(input("How many centimetres would you like to move back? (20cm - 500cm): "))
        if y > 20 and y < 500:
            t.send_command("Back {}".format(y))
        else:
            print("Out of range, try again!(20 - 500) ")
            continue
#insructs the drone to fly forward a specified ammount of cm between 20 and 500
    
    if x.lower() == "cw":
        y = int(input("How many degrees clockwise would you like to turn: (1 - 360):"))
        if y > 1 and y < 360:
            t.send_command("cw {}".format(y))
        else:
            print("Degree invalid, must be  between 1 - 360")
            continue
#instructs the drone to turn clockwise by a specified degree between 1 - 360
    
    if x.lower() == "ccw":
        y = int(input("How many degrees counter-clockwise would you like to turn"))
        if y > 1 and y < 360:
            t.send_command("ccw {}".format(y))
        else:
            print("Degree invalid, must be between 1 - 360")
            continue
#instructs the drone to turn counter clockwise by a specified degree between 1 - 360
    if x.lower() == "land":
        y = input("Would you like to land the drone? 'Y' or 'N'")
        if y != 'Y':
            break
        else:
            continue
#instructs the drone to land
#TODO: add saftey prococol so you cant turn off the program before landing