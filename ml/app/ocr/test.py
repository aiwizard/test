'''
https://webnautes.tistory.com/947
'''


try:
	import Image
except ImportError:
	from PIL import Image
	print('from PIL import Image')
import pytesseract


# 영어 인식
print("recognize ... \n\n")
output = pytesseract.image_to_string(Image.open('example_english.png'))
print("result: ", output)


# 한글 
print("recognize ... \n\n")
pytesseract.image_to_string(Image.open('example_hangul.png'), lang='Hangul')
print("result: ", output)

