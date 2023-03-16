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
    tl_flight.forward(distance=50).wait_for_completed()
    for i in range(0, 302):
        tl_flight.rotate(angle=i+1).wait_for_completed()
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        file_name = "C:\\Users\\Teacher\\Desktop\\save\\image" + "_" + str(i+1) + '.jpg'
        cv2.imwrite(file_name, img)  # 以上面的檔案名，儲存切割的圖片
        cv2.waitKey(1)
    
    
    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()

    tl_drone.close()
