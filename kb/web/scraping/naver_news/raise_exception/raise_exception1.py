'''
https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=python+exception+raise

https://responding.tistory.com/48
https://windorsky.tistory.com/41
https://blog.naver.com/wideeyed/221576227901
https://nwnwlee.tistory.com/36
'''

while True:
    what = input("숫자 입력: ")

    try:
        if int(what) == 1:
            raise ValueError
        elif int(what) == 2:
            raise TypeError
        elif int(what) == 3:
            raise NameError
        
        print("입력 값은: ", float(what))
    except ValueError:
        print('error 1')
    except TypeError:
        print('error 2')
    except NameError:
        print('error 3')
    else:
        break
    finally:
        print('----------------------')
