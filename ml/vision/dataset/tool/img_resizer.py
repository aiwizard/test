
import cv2
import argparse


def arg_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="input image")
    ap.add_argument("-o", "--output", required=True, help="output image")
    ap.add_argument("-x", "--scale", required=True, help="scale: 0.5")
    args = vars(ap.parse_args())

    return args


def check(image, filepath):
    if image is None:
        print("%s is None" %filepath)
        exit()


def main():
    args = arg_parse()

    input_img = args["input"]
    output_img = args["output"]
    xscale = float(args["scale"])
    yscale = float(args["scale"])


    img1 = cv2.imread( input_img )
    check(img1, input_img)

    #img2 = cv2.resize(img1, None, fx=0.4, fy=0.4)
    img2 = cv2.resize(img1, None, fx=xscale, fy=yscale)

    height1, width1, channels1 = img1.shape
    height2, width2, channels2 = img2.shape

    print("({},{}) ---> ({},{})".format(width1, height1, width2, height2))

    cv2.imwrite( output_img , img2)
    check(img2, output_img)


if __name__ == '__main__':
    main()
