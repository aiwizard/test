
## 우분투 저장소 변경
	기존 백업
		sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
	SED(streamlined editor)를 이용해서 kr.archive.ubuntu.com 를 mirror.kakao.com 로 교체
		sed 's(찾을대상)/(교체대상)/g' 파일
		sudo sed -i 's/kr.archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
		cat /etc/apt/sources.list
	확인
		sudo apt-get update
		sudo apt-get upgrade
		apt list --upgradable

## 설치
	dpkg -l	설치된 패키지 리스트
	dpkg -L [패키지이름]	설치된 패키지 경로
	apt-cache search [패키지이름]	패키지 찾기


## Install s/w
### 아래아 한글 뷰어
	sudo apt install gdebi	(dependency 까지 설치해주는 패키지)
	sudo gdebi hancomoffice-hwpviewer-Ubuntu-amd64.deb
	or
	sudo dpkg -i hancomoffice-hwpviewer-Ubuntu-amd64.deb

### PyQt5
	sudo apt install python3-pyqt5

### Qt
	sudo ./qt-unified-linux-x64-3.2.3-online.run


sudo dpkg -i ./google-chrome-stable_current_amd64.deb
sudo snap install chromium

wget https://zoom.us/client/latest/zoom_amd64.deb
sudo apt install ./zoom_amd64.deb 

sudo apt install tmux
sudo apt install r-studio

sudo apt install python3-pip

pip install pygame
pip install PySimpleGUI
sudo apt install tkinter
pip install tkinter
pip install python-tk
sudo apt install python3-tk

pip install seaborn

pip install matplotlib
sudo apt install ffmpeg
sudo apt install mpg321

pip install pytube3
pip install librosa
sudo apt install vim
pip install pyinstaller
pip install gTTS
pip install speechrecognition
pip install playsound
sudo apt-get install python3-pyaudio
sudo apt install net-tools
pip install flask
sudo apt install xcb

pip install hgtk

sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev

sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert
sudo apt install tesseract-ocr-kor
sudo pip3 install pytesseract


