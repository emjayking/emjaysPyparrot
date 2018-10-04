#this is an experiment with the auto launch on feature

from pyparrot.Minidrone import Mambo

mamboAddr = "e0:14:bc:c5:3d:cb"
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    print("getting updates")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("ready for takeoff!")
    mambo.turn_on_auto_takeoff()
    mambo.hover()
    mambo.smart_sleep(15)
    while True:
        if mambo.sensors.flying_state is  "hovering":

            print("landing!")
            mambo.safe_land(5)
            mambo.sleep(5)
            break
            mambo.disconnect()
