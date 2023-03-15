import robomaster
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_flight = tl_drone.flight

    # 起飞后降落
    tl_flight.takeoff().wait_for_completed()
    tl_flight.land().wait_for_completed()

    tl_drone.close()
