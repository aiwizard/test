
## 우분투 설치 후, 해야 할 것들
	https://luckyyowu.tistory.com/409

## 우분투 저장소 변경 및 update/upgrade
	1. 기존 백업
		sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
	2. SED(streamlined editor)를 이용해서 kr.archive.ubuntu.com 를 mirror.kakao.com 로 교체
		sed 's(찾을대상)/(교체대상)/g' 파일
		sudo sed -i 's/kr.archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
		cat /etc/apt/sources.list
	3. 확인
		sudo apt-get update
		apt list --upgradable
		sudo apt-get upgrade

## 설치 관련 커맨드
	dpkg -l	설치된 패키지 리스트
	dpkg -L [패키지이름]	설치된 패키지 경로
	apt-cache search [패키지이름]	패키지 찾기


### venv 설치 및 가상환경 생성/활성화
	sudo apt install python3-venv
	python -m venv <virtual-env-name>
	리눅스
		cd <virtual-env-name>/bin
		source ./activate
	윈도우
		cd <virtual-env-name>\Scripts
		activate
		

## Install s/w
### 아래아 한글 뷰어
	sudo apt install gdebi	(dependency 까지 설치해주는 패키지)
	sudo gdebi hancomoffice-hwpviewer-Ubuntu-amd64.deb
	or
	sudo dpkg -i hancomoffice-hwpviewer-Ubuntu-amd64.deb

### PyQt5
	sudo apt install python3-pyqt5

### Qt
	sudo apt install build-essential
	sudo apt install libfontconfig1		//Generic font configuration library
	sudo apt install mesa-common-dev	//OpenGL library
	sudo install libglu1-mesa-dev -y	//Additional package
	sudo ./qt-unified-linux-x64-3.2.3-online.run

### opencv
	pip install opencv-python
	pip install opencv-contrib-python

### 기타
	sudo dpkg -i ./google-chrome-stable_current_amd64.deb
	sudo snap install chromium

	wget https://zoom.us/client/latest/zoom_amd64.deb
	sudo apt install ./zoom_amd64.deb 
	sudo apt install tmux
	sudo apt install r-studio
	sudo apt install python3-pip
	sudo apt install tkinter
	sudo apt install python3-tk
	sudo apt install ffmpeg
	sudo apt install mpg321
	sudo apt install xcb
	sudo apt-get install python3-pyaudio
	sudo apt install net-tools
	sudo apt install vim
	sudo snap install wps-office

	pip install pygame
	pip install PySimpleGUI
	pip install tkinter
	pip install python-tk
	pip install seaborn
	pip install matplotlib
	pip install pytube3
	pip install librosa
	pip install pyinstaller
	pip install gTTS
	pip install speechrecognition
	pip install playsound
	pip install flask

	pip install hgtk

	sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev

	sudo apt install tesseract-ocr
	sudo apt install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert
	sudo apt install tesseract-ocr-kor
	sudo pip3 install pytesseract
	
	pip install Selenium
	sudo apt install chromium-chromedriver
	cp /usr/lib/chromium-browser/chromedriver /usr/bin
	
