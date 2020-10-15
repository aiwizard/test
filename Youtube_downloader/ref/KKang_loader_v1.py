# Youtube 링크 이용하여 mp3 파일 다운받기
# pytube 사용법 예제 아래 싸이트 참고
# https://simply-python.com/2019/01/02/downloading-youtube-videos-and-converting-to-mp3/
# mp4 -> mp3 변환용 ffmpeg.exe 파일 다운 싸이트
# https://ffmpeg.zeranoe.com/builds/
# Source modified by 네이버 블로그 "코딩 읽어주는 아재" (2020-06-27)


import os
import subprocess
import re

import pytube 
# from moviepy.editor import *


def main():     

    mp3Folder = "D://my_mp3/"

    ytLinkList = ['https://www.youtube.com/watch?v=PO-G3OYqtSM',
                  'https://www.youtube.com/watch?v=3DOkxQ3HDXE',
                  'https://www.youtube.com/watch?v=ftQF5AbDMLM',
                  'https://www.youtube.com/watch?v=hoLzH1revMg']
    
    no_song = 0
    # download youtube video 
    for utlist in ytLinkList:
        youtube = pytube.YouTube(utlist)
        videoTitle = youtube.title
        video = youtube.streams.first()
        # video = yt.streams.filter(only_audio=True).all()
        freshDownload = video.download(output_path=mp3Folder)

        # 다운시 제목이 YouTube.mp4로 동일한 경우 숫자 추가
        if str(freshDownload).find('YouTube.mp4'):        
            no_song += 1
            name = str(freshDownload).split('.')[0]+str(no_song)
            name = name+'.mp4'
            os.rename(str(freshDownload), name)
            print('Downloaded: ', name)
        else:
            print('Downloaded: ', str(freshDownload))
        
    # 폴더내 mp4 파일 찾아 ffmpeg.exe로 mp3 변환하기
    for file in [n for n in os.listdir(mp3Folder) if re.search('mp4',n)]:
        mp4_path = os.path.join(mp3Folder, file)
        mp3_path = os.path.join(mp3Folder,os.path.splitext(file)[0]+'.mp3')
        subprocess.run(['ffmpeg', '-i', mp4_path, mp3_path])
        print("Converting: ", mp4_path, " to ", mp3_path)
        
    # 폴더내 mp4 파일 찾아 삭제, 필요시 아래 코드 block
    for file in [n for n in os.listdir(mp3Folder) if re.search('mp4',n)]:
        mp4d_path = os.path.join(mp3Folder, file)
        os.remove(mp4d_path)
        print("Deleting: ", mp4d_path)
        
    # clip = VideoFileClip(full_path).subclip(0, 20)
    # video = AudioFileClip(full_path)
    # video.audio.write_audiofile(output_path)


if __name__ == '__main__':
    main()
    
