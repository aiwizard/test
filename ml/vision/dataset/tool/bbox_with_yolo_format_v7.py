import cv2
import sys
import os
import time
import matplotlib.pyplot as plt
import argparse


splash_image = "m5.jpg"
#ext_str = ""


def arg_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--target", required=True, help="file or dir")
    ap.add_argument("-e", "--extention", required=True, help="specify the extention of image file to use")
    args = vars(ap.parse_args())

    return args


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
    print("\t{}, {}".format(dw, dh))

    labelfile = filepath.replace(ext_str, ".txt")
    fl = open(labelfile, 'r')
    labels = fl.readlines()
    fl.close()

    for label in labels:
        # Split string to float
        #_, x, y, w, h = map(float, label.split(' '))
        food_class, x, y, w, h = map(float, label.split(' '))
        print("\t{}, {}, {}, {}".format(x,y,w,h))

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

        print("\t{}, {}, {}, {}".format(l,t,r,b))
        #cv2.rectangle(img, (l, t), (r, b), (255, 0, 255), 2)
        cv2.rectangle(img, (l, t, r-l, b-t), (255, 0, 255), 1)
        #cv2.putText(img, food[food_class], (l, t-8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, 1);


    #색상이 이상하게 나온다
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    #plt.show()

    #img = cv2.resize(img, (800,600))
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
    img = cv2.imread(splash_image, cv2.IMREAD_COLOR)
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
    #print("ext_str: ", ext_str)
    for f in os.listdir(dirpath):
        full_filename = os.path.join(dirpath, f)
        ext = os.path.splitext(full_filename)[-1]
        if ext == ext_str:
            filelist.append(full_filename)

    if len(filelist) == 0:
        print("There is no {} file".format(ext_str))
        return

    img = cv2.imread(splash_image, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)

    i=-1 #처음 'd' 누르면, 무조건 next 이므로
    size = len(filelist)
    print(filelist, size, i)
    while True:
        key = cv2.waitKey(0)
    
        if key == ord('q'):
            print("bye")
            break
        elif key == ord('a'):
            i -= 1
        elif key == ord('d'):
            i += 1
        else:
            print("You can press (a | d)")


        if i < 0: i=0
        if i > size-1: i=size-1

        print(filelist[i])
        cv2.destroyAllWindows()
        draw_bbox(filelist[i], i)
        time.sleep(0.01)

    cv2.destroyAllWindows()



def main():
    #if(len(sys.argv) != 3):
    #    print("usage: {} <file | dir> JPG|PNG|...".format(sys.argv[0]))
    #    return

    args = arg_parse()

    filepath = args["target"]
    global ext_str
    ext_str = ".{}".format(args["extention"])

    if( filepath.find(ext_str) == -1):
        draw_bbox_dir(filepath)    # dir path
    else:
        draw_bbox_file(filepath)    # file path


if __name__ == '__main__':
    main()
