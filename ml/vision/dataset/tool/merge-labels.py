'''
    [usage] python get-yolo-label.py

    1, 2, 3 ... 폴더 의 parrent 폴더에서 실행할 것
    out: all.txt
'''

import os


for i in range(1, 101):
    cmdstr = "{}".format(i)
    os.chdir(cmdstr)
    
    cmdstr = "echo [{}] >> ../all.txt".format(i)
    os.system(cmdstr)
    
    cmdstr = "for %f in (*.txt) do type %f >> ../all.txt"
    os.system(cmdstr)
    
    os.chdir("../")
