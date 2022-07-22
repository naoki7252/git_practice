import cv2
import os
import time 
import sys

def save_frame_camera_cycle(device_num, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        print("fail to open camera")
        sys.exit(1)
        
    n = 0
    while True:
        ret, frame = cap.read()
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): break

        elif key == ord('t'):
            cv2.imwrite(f"C:\\Users\\satounaoki\\Desktop\\sisoukai\\camera_1\\sample_img{n}.jpg", frame)
            n += 1
            
        cv2.imshow(window_name, frame)
        
    cap.release()
    cv2.destroyWindow(window_name)


def main():
    save_frame_camera_cycle(0)


if __name__ == '__main__':
    main()
