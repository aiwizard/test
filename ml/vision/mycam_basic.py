import sys
import cv2


def video_on():
    # 기본 카메라 객체 생성
    cap = cv2.VideoCapture(0)	# 0이면 내장 웹캠, 숫자를 올리면 추가된 웹캠 이용 가능
    if not cap.isOpened():  # 카메라가 열렸는지 확인
        print("Camera open failed!")
        sys.exit()


    while True:
        ret, frame = cap.read()
        if not ret: # 새로운 프레임을 못받았으면
            break

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
        
    cap.release()




video_on()


cv2.waitKey(0)
cv2.destroyAllWindows()

