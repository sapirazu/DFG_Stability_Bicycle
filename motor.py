from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging

def move_platform(mots, dirction, angel,speed):
    # mots=connect()
    step=angel*14000
    match dirction:
        case 'f':
            # move forward
            position_0=150000+step
            position_1=150000+step
            pass
        case 'b':
            # move backward
            position_0=150000-step
            position_1=150000-step
            pass
        case 'l':
            # move left
            position_0=150000-step
            position_1=150000+step
            pass
        case 'r':
            # move right
            position_0=150000+step
            position_1=150000-step
            pass
        case 'h':
            # move home
            position_0=150000
            position_1=150000
            pass

    mots[0].position_task(position_0, speed, absolute=True, nonblocking=True)
    mots[1].position_task(position_1, speed, absolute=True, nonblocking=True)
    target_positions_reached = [mot.target_position_reached() for mot in mots]
    # while True:
    #     target_positions_reached = [mot.target_position_reached() for mot in mots]
    #     if all(target_positions_reached):
    #         break

def connect():
    coms = [ComModbus(ip_address='192.168.0.11'),   # Right motor
            ComModbus(ip_address='192.168.0.3')]    # Left motor
    
    for com in coms:
       if not com.connected():
        exit()
    mots = [MotionHandler(com) for com in coms]

    for mot in mots:
       mot.acknowledge_faults()
       mot.enable_powerstage()
       if not mot.referenced():
        mot.referencing_task()
    return mots

if __name__ == "__main__":
    mots = connect()

    for mot in mots:
        mot.shutdown()