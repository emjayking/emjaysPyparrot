#This is a trial script for the parrot drones. I want to run them using python.
#To do this I'm going run the codes on my raspberry pi
# I will controll the Pi using my laptop (via VNC or SSH)
# Eventually I want to use a custom made controller and a raspberry pi to controll the parrot drone
# and I also want to make an auto flying feature to complete various objectives.


#27/09/18
# the plan is to try and find a way to use the pyparrot respository in my code.
from pyparrot.Minidrone import Mambo

mamboAddr = "e0:14:bc:c5:3d:cb"
 #3/10/2018 success today managed to connect and run the demo scripts.
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("ready for take-off!")
    # mambo.safe_takeoff(5)
    mambo.turn_on_auto_takeoff()
    mambo.smart_sleep(15)
    print("hovering")
    mambo.hover()
    mambo.smart_sleep(2)

    # try:
    #    battery = mambo.sensors.battery()
    #    print("battery %s" % battery)
    # except:
    #    print("battery failed")


    print("landing?")

    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnecting")
    mambo.disconnect()
else:
    print("failed")
