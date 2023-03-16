import robomaster
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_flight = tl_drone.flight

    # 起飞
    tl_flight.takeoff().wait_for_completed()

    # 向前飞50厘米，向后飞50厘米
    tl_flight.forward(distance=50).wait_for_completed()
    tl_flight.backward(distance=50).wait_for_completed()

    # 降落
    tl_flight.land().wait_for_completed()

    tl_drone.close()
