import robomaster
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_flight = tl_drone.flight

    # 起飞
    tl_flight.takeoff().wait_for_completed()

    # 上升20厘米，下降20厘米
    tl_flight.up(distance=20).wait_for_completed()
    tl_flight.down(distance=20).wait_for_completed()

    # 降落
    tl_flight.land().wait_for_completed()

    tl_drone.close()
