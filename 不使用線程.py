import cv2
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()
    tl_flight = tl_drone.flight
    tl_flight.takeoff().wait_for_completed()
    tl_camera = tl_drone.camera
    # 显示302帧图传
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)
    for i in range(0, 302):
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        file_name = "C:\\Users\\Teacher\\Desktop\\save\\image" + "_" + str(i + 1) + '.jpg'
        cv2.imwrite(file_name, img)
        tl_flight.rotate(angle=10).wait_for_completed()
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()
    tl_drone.close()

