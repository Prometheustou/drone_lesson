import cv2
from robomaster import robot
import threading
from time import sleep


class MyThread1(threading.Thread):
    def run(self):
        tl_camera = tl_drone.camera
        # 显示302帧图传
        tl_camera.start_video_stream(display=False)
        tl_camera.set_fps("high")
        tl_camera.set_resolution("high")
        tl_camera.set_bitrate(6)
        k=1
        for i in range(0, 2300):
            img = tl_camera.read_cv2_image()
            cv2.imshow("Drone", img)
            if i % 10 == 0:
                file_name = "C:\\Users\\Teacher\\Desktop\\save\\image_" + str(k) + ".jpg"
                cv2.imwrite(file_name, img)
                k = k+1
            cv2.waitKey(1)
        cv2.destroyAllWindows()
        tl_camera.stop_video_stream()
        tl_drone.close()


class MyThread2(threading.Thread):
    def run(self):
        for i in range(40):
            tl_flight.rotate(angle=10).wait_for_completed()
            sleep(1)
        tl_flight.land().wait_for_completed()


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()
    tl_flight = tl_drone.flight
    tl_battery = tl_drone.battery.get_battery()
    print("begin battery soc: {0}".format(tl_battery))
    tl_flight.takeoff().wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.up(distance=50).wait_for_completed()
    threadl = []
    t1 = MyThread1()
    t2 = MyThread2()
    threadl.append(t1)
    threadl.append(t2)
    for x in threadl:
        x.start()
    #tl_battery = tl_drone.battery.get_battery()
    #print("end battery soc: {0}".format(tl_battery))
    # 起飞后降落
