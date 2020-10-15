위젯
	https://blog.naver.com/shining0721/221958907424


위젯 state
	https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/

		
전반 참고
	https://www.programcreek.com/python/example/12383/Tkinter.DISABLED
	https://docs.python.org/ko/3.9/contents.html
	
	
람다, 위젯 state
	https://jakestistory.tistory.com/197
	
	
지뢰찾기 소스
	https://jaraworkshop.tistory.com/4
	
	
-------------------------------------------------------------------------- usage
실행파일 만들기
	pyinstaller [--onefile] downloader.py


------------------------------------------------------------------------------------------------ 에러 수정
1. KeyError 에러
	parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
	KeyError: 'cipher'

	==> 
		pip show pytube3 로 lib 위치를 찾아서 extract.py 의 내용을 아래와 같이 수정하면 됨
		parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
		==>
		parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)

	참고: https://stackoverflow.com/questions/62098925/why-my-youtube-video-downloader-only-downloads-some-videos-and-for-other-videos


2. 에러
	https://www.youtube.com/watch?v=gRpa42TsT9g
	
