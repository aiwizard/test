
## 우분투 설치 후, 해야 할 것들
	https://luckyyowu.tistory.com/409
		1. Google Chrome 설치
		2. apt 소스 저장소를 카카오 미러 서버로 변경
		3. 몇 가지 기본 패키지 설치와 전체 업데이트
		4. uim 입력기 설치 및 uim 벼루 설정
		5. zsh과 oh-my-zsh 설치, 그리고 플러그인 적용
			5-1. zsh bullet-train 테마
			5-2. 조금 도움되는 플러그인 들
			5-3. Powerline 폰트 설치
		6. snap으로 몇 가지 개발 도구들 설치
		7. Node.js 개발 환경 구축
		8. TLP(노트북 배터리 최적화 패키지) 설치
		

## 우분투 저장소 변경 및 update/upgrade
	1. 기존 저장소 백업
		sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
	2. SED(streamlined editor)를 이용해서 kr.archive.ubuntu.com 를 mirror.kakao.com 로 교체
		sed 's(찾을대상)/(교체대상)/g' 파일
		sudo sed -i 's/kr.archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
		cat /etc/apt/sources.list
	3. 확인
		sudo apt update
		apt list --upgradable
		sudo apt upgrade

## 설치 관련 커맨드
	dpkg -l			설치된 패키지 리스트
	dpkg -L [패키지이름]		설치된 패키지 경로
	apt-cache search [패키지이름]	패키지 찾기


## Install s/w
### 크롬
	chrome 검색해서 .deb 파일 받을 것
	
	아래는 크로미엄
	sudo dpkg -i ./google-chrome-stable_current_amd64.deb
	or
	sudo snap install chromium

### Install prerequisites
	sudo apt install python3-pip
	pip3 install -r requirements.txt
	python3 -c "import nltk; nltk.download('punkt')"

### venv 설치 및 가상환경 생성/활성화
	설치	sudo apt install python3-venv
	생성	python3 -m venv <virtual-env-name>
	리눅스
		cd <virtual-env-name>/bin
		source ./activate
	윈도우
		cd <virtual-env-name>\Scripts
		activate
	

### 아래아 한글 뷰어 (20.04 에서는 미지원)
	sudo apt install gdebi	(dependency 까지 설치해주는 패키지)
	sudo gdebi hancomoffice-hwpviewer-Ubuntu-amd64.deb
	or
	sudo dpkg -i hancomoffice-hwpviewer-Ubuntu-amd64.deb

### PyQt5
	sudo apt install python3-pyqt5
	or ???
	pip3 install pyqt5	//PyQt5 설치
	pip3 install pyqt5-tools	//QT Designer 설치
	
	
	pip3 install --user pyqt5
	sudo apt install python3-pyqt5
	sudo apt install pyqt5-dev-tools
	sudo apt install qttools5-dev-tools
	
	2. pip install --user 과 sudo pip install
		https://blog.naver.com/cjw531/222089537154
		--user 이 대체 무엇이기에 Environment Error 가 나는 것인가?
		pip3 는 기본적으로 시스템 디렉토리 (ex. /usr/local/lib/python3.7) 에 Python package 를 설치한다. root premission 이 필요하다.
		--user 는 홈 디렉토리에 pip3 install package 를 대신 만들어 root permission 이 필요하지 않다.
		그럼 root permission 만 간단히 주면 되니까 sudo pip install 을 사용하면 되지 않는가? 라고 생각할 수도 있다. 안된다. 절대 sudo pip install 을 하면 안된다.
		물론 sudo pip install 을 해도 아래와 같이 설치는 잘 된다

### Qt
	sudo apt install build-essential
	sudo apt install libfontconfig1	//Generic font configuration library
	sudo apt install mesa-common-dev	//OpenGL library
	sudo install libglu1-mesa-dev -y	//Additional package
	sudo ./qt-unified-linux-x64-3.2.3-online.run

### opencv (파이썬 버전)
	pip3 install opencv-python
	pip3 install opencv-contrib-python

### 기타
	wget https://zoom.us/client/latest/zoom_amd64.deb
	sudo apt install ./zoom_amd64.deb 
	
	sudo apt install mpg321
	sudo apt install xcb		// qt plugin 설치 문제시
	sudo apt install net-tools
	sudo apt install vim

	sudo apt install tmux	(like gnu screen)
	sudo apt install r-studio
	sudo snap install wps-office

	sudo apt install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev

	sudo apt install tesseract-ocr
	sudo apt install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert
	sudo apt install tesseract-ocr-kor
	pip3 install pytesseract

	
v	pip3 install pygame
	pip3 install pysimplegui
v	pip3 install guizero
	sudo apt install tkinter	// python2 ??
v	sudo apt install python3-tk

	pip3 install seaborn
	pip3 install matplotlib

v	pip3 install pytube3
v	sudo apt install ffmpeg
	pip3 install pyinstaller


	pip3 install playsound	//재생, https://github.com/TaylorSMarks/playsound
	pip3 install pyaudio	//녹음, portaudio의 파이썬 버전
			https://kcal2845.tistory.com/35
			http://people.csail.mit.edu/hubert/pyaudio/
	pip3 install librosa
	pip3 install gTTS
	pip3 install speechrecognition

	pip3 install flask

	pip3 install hgtk

	pip3 install Selenium
	sudo apt install chromium-chromedriver
	cp /usr/lib/chromium-browser/chromedriver /usr/bin
	
