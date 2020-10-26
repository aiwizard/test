import time
from tqdm import tqdm

num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in tqdm(num):
    time.sleep(1)
    
for i in tqdm(range(10)):
    #print(i)
    time.sleep(1)
