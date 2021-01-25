import argparse

def arg_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="image path")
    ap.add_argument("-n", "--name", required=False, help="name please")
    args = vars(ap.parse_args())

    return args


def main():
    args = arg_parse()

    print("image: {}".format(args["image"]))
    print("name: {}".format(args["name"]))


if __name__ == '__main__':
    main()
