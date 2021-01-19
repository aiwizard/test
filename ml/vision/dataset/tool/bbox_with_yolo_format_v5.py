import cv2
import sys
import os
import time
import matplotlib.pyplot as plt


def get_name():
    f = open("food100.names", 'r')
    names = f.readlines()
    f.close()

    i = 0
    food = {}
    for n in names:
        n = n.strip()
        food[i] = n
        i+=1

    return food


def draw_bbox(filepath, idx):
    food = get_name()

    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    dh, dw, _ = img.shape
    print("{}, {}".format(dw, dh))

    labelfile = filepath.replace(".JPG", ".txt")
    fl = open(labelfile, 'r')
    labels = fl.readlines()
    fl.close()

    for label in labels:
        # Split string to float
        #_, x, y, w, h = map(float, label.split(' '))
        food_class, x, y, w, h = map(float, label.split(' '))
        print("{}, {}, {}, {}".format(x,y,w,h))

        # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
        # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)
        
        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1

        print("{}, {}, {}, {}".format(l,t,r,b))
        #cv2.rectangle(img, (l, t), (r, b), (255, 0, 255), 2)
        cv2.rectangle(img, (l, t, r-l, b-t), (255, 0, 255), 1)
        #cv2.putText(img, food[food_class], (l, t-8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, 1);


    #색상이 이상하게 나온다
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    #plt.show()

    img = cv2.resize(img, (800,600))
    caption = "bbox on image - {}, {}".format(filepath, idx+1)
    cv2.imshow(caption, img)
    cv2.moveWindow(caption, 100,50)


    '''
    if( cv2.waitKey(0) == 27 ):	# 27: ESC
        cv2.destroyAllWindows()
        return 0

    cv2.destroyAllWindows()
    '''


def draw_bbox_file(filepath):
    img = cv2.imread('m5.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('image', img)

    while True:
        key = cv2.waitKey(0)
    
        if key == ord('q'):
            print("bye")
            break
        
        cv2.destroyAllWindows()
        draw_bbox(filepath, 0)
        time.sleep(0.01)

    cv2.destroyAllWindows()


def draw_bbox_dir(dirpath):
    filelist = []

    for f in os.listdir(dirpath):
        full_filename = os.path.join(dirpath, f)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.JPG':
            filelist.append(full_filename)

    img = cv2.imread('m5.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('image', img)

    i=0
    size = len(filelist)
    while True:
        key = cv2.waitKey(0)
    
        if key == ord('q'):
            print("bye")
            break
        elif key == ord('a'):
            if( i-1 > 0 ):
                i -= 1
            else:
                print("first file")
        elif key == ord('d'):
            if( i+1 < size ):
                i += 1
            else:
                print("last file")
        else:
            print("skip")

        print(filelist[i])
        cv2.destroyAllWindows()
        draw_bbox(filelist[i], i)
        time.sleep(0.01)

    cv2.destroyAllWindows()


############################################
'''
def show_img(is_next):
    if is_next == 1:
        print("-->")
        # 다음 이미지
    elif is_next == 2:
        print("<--")
        # 이전 이미지


def main():
    img = cv2.imread('m5.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('image', img)


    while True:
        key = cv2.waitKey(0)
    
        if key == ord('q'):
            print("bye")
            break
        elif key == ord('a'):
            show_img(1)
        elif key == ord('d'):
            show_img(2)
        else:
            print("skip")

    cv2.destroyAllWindows()
'''
############################################


def main():
    filepath = sys.argv[1]
    if( filepath.find(".JPG") == -1):
        if( filepath.find(".png") == -1):
            draw_bbox_dir(filepath)    # dir path
    else:
        draw_bbox_file(filepath)    # file path


if __name__ == '__main__':
    main()
