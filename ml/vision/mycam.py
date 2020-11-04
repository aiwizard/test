import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


def test_ocr(img):
    try:
        import Image
    except ImportError:
        from PIL import Image
        print('from PIL import Image')

    import pytesseract

    # 영어 인식
    #print("recognize ... \n\n")
    #output = pytesseract.image_to_string(Image.open('./52.jpg'))
    #print("result: ", output)

    # 한글 
    print("recognize ... \n\n")
    output = pytesseract.image_to_string(Image.open('./images/52.jpg'), lang='Hangul')
    print("result: ", output)


 
def image_edges(img):
    dst = cv2.Canny(img,100,200)
    #cv2.imwrite('./out_edge.jpg', dst)
    return dst

def image_affine_transformation1(img):
    rows,cols = img.shape
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv2.getAffineTransform(pts1,pts2)
    dst = cv2.warpAffine(img,M,(cols,rows))
    #cv2.imwrite('./out_affine_trans1.jpg', dst)
    return dst

def image_affine_transformation2(img):
    rows,cols = img.shape
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(cols,rows))
    #cv2.imwrite('./out_affine_trans2.jpg', dst)
    return dst

'''
    resize - scale transformation & save
    https://mr-waguwagu.tistory.com/13
    https://deep-learning-study.tistory.com/185
'''
def image_resize(img):
    dst1 = cv2.resize(img, dsize=(640, 480))
    dst2 = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imwrite('./images/out_resize-1org.jpg', img)
    cv2.imwrite('./images/out_resize-2dsize.jpg', dst1)
    cv2.imwrite('./images/out_resize-3scale_0.5.jpg', dst2)
    return dst2

def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3) # 밝은 곳은 더 밝게 어두운 곳은 더 어둡게 해야 스케치스러운 느낌을 받을 수 있다
    dst = cv2.divide(gray, blr, scale=255) # 흑백영상을 블러로 나눈 값을 255로 곱함.
    #cv2.imwrite('./images/out_pencil_sketch.jpg', dst)
    return dst

def pencil_sketch_color(img):
    blr = cv2.GaussianBlur(img, (0, 0), 3) # 밝은 곳은 더 밝게 어두운 곳은 더 어둡게 해야 스케치스러운 느낌을 받을 수 있다
    dst = cv2.divide(img, blr, scale=255) # 흑백영상을 블러로 나눈 값을 255로 곱함.
    #cv2.imwrite('./images/out_pencil_sketch_color.jpg', dst)
    return dst

def to_grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('./out_grayscale.jpg', gray)
    return gray
    
# https://hoony-gunputer.tistory.com/entry/OpenCv-python-기초-이미지-읽고-저장하기
def show_matplotlib(img):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()



def apply_effect(frame, mode):
    if mode == 1:   # edge
        frame = image_edges(frame)
    elif mode == 2: # 윤곽선 추출 (contour)
        frame = cv2.Canny(frame, 50, 150)
    elif mode == 3:	# 반전
        frame = ~frame
    elif mode == 4: # 스케치 필터
        frame = pencil_sketch(frame)
    elif mode == 5: # 스케치 필터 color
        frame = pencil_sketch_color(frame)
    elif mode == 6: # grayscale
        frame = to_grayscale(frame)

    return frame


'''
https://hoony-gunputer.tistory.com/entry/OpenCv-python-기초-노트북-웹캠을-이용해서-동영상을-읽고-쓰기
https://thebook.io/006939/ch04/01/04-02/

https://deep-learning-study.tistory.com/107
https://deep-learning-study.tistory.com/174
https://deep-learning-study.tistory.com/108
https://deep-learning-study.tistory.com/category/Computer%20Vision/파이썬%20OpenCV%20공부
https://deep-learning-study.tistory.com/category/Computer%20Vision/OpenCV%20머신러닝%20실습
'''
def cam_video():
    # 기본 카메라 객체 생성
    cap = cv2.VideoCapture(0)	# 0이면 내장 웹캠, 숫자를 올리면 추가된 웹캠 이용 가능
    if not cap.isOpened():  # 카메라가 열렸는지 확인
        print("Camera open failed!")
        sys.exit()
        
    # 웹캠의 속성 값을 받아오기
    # 정수 형태로 변환하기 위해 round
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) # 카메라에 따라 값이 정상적, 비정상적

    # for save
    # fourcc 값 받아오기, *는 문자를 풀어쓰는 방식, *'DIVX' == 'D', 'I', 'V', 'X'
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc(*'H264')

    # 1프레임과 다음 프레임 사이의 간격 설정
    delay = round(1000/fps)
    print('w: {}, h: {}'.format(w,h))
    print('fps: ', fps)
    print('delay: ', delay)

    # 웹캠으로 찰영한 영상 저장
    #video = cv2.VideoWriter('./mycam.avi', fourcc, fps, (w, h))
    video = cv2.VideoWriter('./mycam.mpg', fourcc, fps, (w, h))

    cam_mode = 0

    while True:
        ret, frame = cap.read()
        if not ret: # 새로운 프레임을 못받았으면
            break

        ############### text and rectangle
        cv2.rectangle(frame, (100, 100, 50, 100), (0, 255, 0), 2)
        text = "hello"
        cv2.putText(frame, text, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
            (0, 0, 255), 1, cv2.LINE_AA)
        ###############

        frame = apply_effect(frame, cam_mode)
        cv2.imshow('frame', frame)

        video.write(frame)	# save

        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == ord(' '):	#스페이스 누르면
            cam_mode += 1	# 모드가 1 증가
            if cam_mode == 7: 
                cam_mode = 0
        
    cap.release()



'''
# load ##################################################
imgColor = cv2.imread('./images/52.jpg')
imgGray = cv2.imread('./images/52.jpg', cv2.IMREAD_GRAYSCALE)   # 0: gray, 1: color
#########################################################


#1 original
cv2.imshow('original-color', imgColor)
cv2.imshow('original-gray', imgGray)


#2. edges and show
dst = image_edges(imgGray)
cv2.imshow('edge', dst)


#3 Affine Transformation
dst = image_affine_transformation1(imgGray)
cv2.imshow('image_affine_transformation1', dst)

dst = image_affine_transformation2(imgGray)
cv2.imshow('image_affine_transformation2', dst)


#4 resize, scale_transformation
dst = image_resize(imgGray)
cv2.imshow('resize - scale transformation', dst)


#5 pencil_sketch
dst = pencil_sketch(imgColor)
cv2.imshow('pencil_sketch', dst)
dst = pencil_sketch_color(imgColor)
cv2.imshow('pencil_sketch color', dst)


#6 to grayscale
dst = to_grayscale(imgColor)
cv2.imshow('grascale', dst)


#7 OCR
test_ocr(imgGray)


#print('img:', imgColor)             # 이미지 데이터를 확인
print('type(img):', type(imgColor))  # 데이터 타입을 확인
print('img.shape:', imgColor.shape)  # 차원을 확인 (해상도)
'''

#8 Show using matplotlib
#show_matplotlib(imgGray)	# 에러 발생

#9 Notebook web cam video
cam_video()


# END ###################################################
cv2.waitKey(0)
cv2.destroyAllWindows()
#########################################################
