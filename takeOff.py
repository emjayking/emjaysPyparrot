# this is the page for experimenting with various takeoff methods.

from pyparrot.Minidrone import Mambo

mamboAddr = "e0:14:bc:c5:3d:cb"

mambo = Mambo(mamboAddr, use_wifi=False)

print("attempting connection")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off")
    mambo.safe_takeoff(5)
    mambo.sleep(5)

    print("hovering")
    mambo.hover()
    mambo.smart_sleep(5)

    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnecting")
    mambo.disconnect()
