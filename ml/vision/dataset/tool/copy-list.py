'''
    usage: python copy-list.py <file-list> <target_dir>

    sed -i 's/aaa/bbbb/' <file>

'''

import sys
import os


def mycopy(path, target):
    path = path.replace('.jpg', '.*')

    items = path.split("/")

    # null 원소 지우기
    i=0
    for item in items:
        if len(item)==0:
            del items[i]
        i+=1
    

    str_depth = "{}".format(target)
    # 맨 앞 섹션이 .. 이면, skip 하려고
    if(items[0][0] != '.'): i=0
    else: i=1

    while i<len(items)-1:
        tmp = "/{}".format(items[i])
        str_depth += tmp
        #newpath = "/out/{}/{}/{}".format(list[1], list[2], list[3])
        #subdir = "mkdir -p out/{}".format(list[2])
        i+=1

    # 폴더 구조 생성 및 복사
    make_dir = "mkdir -p {}".format(str_depth)
    copy_file = "cp {} {}".format(path, str_depth)
    #print(make_dir)
    print(copy_file)
    os.system(make_dir)
    os.system(copy_file)


def main():
    if len(sys.argv) != 3:
        print("\tusage: python copy-list.py <file-list> <target_dir>\n\n")
        exit()

    filelist = sys.argv[1]
    target = sys.argv[2]

    f = open(filelist, 'r')
    lines = f.readlines()
    for line in lines:
        path = line.strip()
        #print(path)
        mycopy(path, target)
    f.close()


if __name__ == '__main__':
    main()
