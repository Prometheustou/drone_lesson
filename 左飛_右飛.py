import robomaster
from robomaster import robot
if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()
    tl_flight = tl_drone.flight
    # 起飞
    tl_flight.takeoff().wait_for_completed()
    # 向左飞50厘米，向右飞50厘米
    tl_flight.left(distance=50).wait_for_completed()
    tl_flight.right(distance=50).wait_for_completed()
    # 降落
    tl_flight.land().wait_for_completed()
    tl_drone.close()
