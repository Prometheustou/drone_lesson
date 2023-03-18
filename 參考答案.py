import cv2
from robomaster import robot
import time

if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()
    tl_flight = tl_drone.flight

    # 起飞后降落
    tl_flight.takeoff().wait_for_completed()
    tl_camera = tl_drone.camera
    # 显示302帧图传
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)
    for i in range(0, 302):
        tl_battery = tl_drone.battery
        battery_info = tl_battery.get_battery()
        print("Drone battery soc: {0}".format(battery_info))
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        file_name = "C:\\Users\\acer\\Desktop\\save\\image_" + str(i + 1) + ".jpg"
        cv2.imwrite(file_name, img)
        tl_flight.rotate(angle=10).wait_for_completed()
        cv2.waitKey(1)
        #time.sleep(2)

    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()
    tl_flight.land().wait_for_completed()
    tl_drone.close()
