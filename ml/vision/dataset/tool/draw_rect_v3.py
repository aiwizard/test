# https://sikaleo.tistory.com/80

'''영상을 마우스로 드레그한 영역을 grayscale 로 변환하여 새로운 윈도우에 띄우는 프로그램 개발''' 
import os 
import cv2 


start_x, start_y = -1, -1 
pt1, pt2 = (0,0), (0,0)
labels = []



def draw_history(img_result):
    global labels
    # 최근 1개와 다른 것들과의 라인 두께, 색상 차별화
    cnt = 0
    size = len(labels)
    for i in labels:
        if( cnt == size-1):
            cv2.rectangle(img_result, i[0], i[1], (0, 0, 255), 2)
        else:
            cv2.rectangle(img_result, i[0], i[1], (255, 0, 0), 1)
        cnt += 1



def mouse_callback(event, x, y, flags, param): 
    global start_x, start_y, labels, pt1, pt2

    # 버튼 누를 때마다 이미지 새로 그리는 게 핵심
    img_result = param.copy()

    if event == cv2.EVENT_LBUTTONDOWN: 
        start_x, start_y = x, y 
        cv2.circle(img_result, (x, y), 8, (0, 255, 255), -1) 
        cv2.imshow('img_color', img_result) 

    elif event == cv2.EVENT_MOUSEMOVE: 
        h, w, _ = img_result.shape
        cv2.line(img_result, tuple((x,0)), tuple((x,h)), (0,192,0), 1, cv2.LINE_AA)
        cv2.line(img_result, tuple((0,y)), tuple((w,y)), (0,192,0), 1, cv2.LINE_AA)

        if flags & cv2.EVENT_FLAG_LBUTTON:
            left = min(start_x, x)
            top = min(start_y, y)
            right = max(start_x, x)
            bottom = max(start_y, y)
            pt1, pt2 = (left, top), (right, bottom)

            cv2.rectangle(img_result, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.imshow('img_color', img_result)
    
    elif event == cv2.EVENT_LBUTTONUP: 
        # 1. 좌표 저장
        labels.append((pt1, pt2))
        # 파일 처리

        # 2. Next file (자동/수동 option)
        # 3. 이전 좌표 자동 불러오기
        


    draw_history(img_result)

    cv2.imshow('img_color', img_result)



def main():
    path = os.path.join('./', '24.jpg') 
    img_color = cv2.imread(path) 

    cv2.imshow('img_color', img_color) 

    # 콜백 등록시, 이미지를 파라미터로 넘긴다
    cv2.setMouseCallback('img_color', mouse_callback, img_color)

    while True:
        key = cv2.waitKey(0)    #27(ESC), 13(ENTER), 9(TAB)

        if key == 27 or key == ord('q'):
            break
        elif key == ord('r'):
            # 전체 삭제 후, 화면 refresh
            del labels[:len(labels)]
        elif key == ord('i'):
            img_color = ~img_color
            draw_history(img_color)

        
        cv2.imshow('img_color', img_color)


    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
