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
    print(mambo.sensors.flying_state)
    mambo.smart_sleep(10)
    while True:
        print(mambo.sensors.flying_state)
        if mambo.sensors.flying_state !=  "landed":
            print("flying forward")
            mambo.smart_sleep(3)
            mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)

            print("flying backwards")
            mambo.smart_sleep(2)
            mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=1)

            print("turning 360")
            mambo.smart_sleep(2)
            mambo.turn_degrees(180)
            mambo.smart_sleep(2)
            mambo.turn_degrees(180)

    
            print("landing")
            mambo.safe_land(5)
            mambo.smart_sleep(5)

            print("disconnect")
            mambo.disconnect()
