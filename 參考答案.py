import cv2
from robomaster import robot


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    tl_camera = tl_drone.camera
    # 显示302帧图传
    tl_flight = tl_drone.flight
    # 起飞
    tl_flight.takeoff().wait_for_completed()
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)
    for i in range(0, 302):
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        cv2.waitKey(1)
    tl_flight.forward(distance=50).wait_for_completed()
    tl_flight.rotate(angle=360).wait_for_completed()
    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()

    tl_drone.close()
