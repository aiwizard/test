'''
출처
	https://info-lab.tistory.com/230
	http://parkjuwan.dothome.co.kr/wordpress/2017/06/24/text-color-py/
'''

class Colors:
	BLACK = 		'\033[30m'
	RED = 			'\033[31m'
	GREEN = 		'\033[32m'
	YELLOW = 		'\033[33m'
	BLUE = 		'\033[34m'
	MAGENTA = 	'\033[35m'
	CYAN = 		'\033[36m'
	WHITE = 		'\033[37m'
	
	BG_BLACK =	'\33[40m'
	BG_RED =		'\33[41m'
	BG_GREEN =	'\33[42m'
	BG_YELLOW =	'\33[43m'
	BG_BLUE =		'\33[44m'
	BG_PURPLE =	'\33[45m'
	BG_CYAN =		'\33[46m'
	BG_WHITE =	'\33[47m'

	RESET = 		'\033[0m'
	BOLD = 		'\033[1m'
	CANTBEUSED =	'\033[2m'	#사용불가
	ITALIC =	 	'\033[3m'
	UNDERLINE = 	'\033[4m'
	SPLASH1 = 	'\033[5m'
	SPLASH2 = 	'\033[6m'
	REVERSE = 	'\033[7m'	#역상
	HIDE = 		'\033[8m'	#숨기기
	STRIKE = 		'\033[9m'	#취소선


print(Colors.CYAN + "This is the " + Colors.UNDERLINE + Colors.RED + "test" + Colors.RESET)

print(Colors.GREEN)
print("abcde")
print(Colors.RESET)

print("This ended up " + Colors.SPLASH1 + "100%" + Colors.RESET)
print("This ended up " + Colors.SPLASH2 + "100%" + Colors.RESET)

print(Colors.BG_YELLOW + "Good work" + Colors.RESET)
print()

