i = 0
menu = ["냉면", "볶음밥", "피자", "짜장면", "주문취소"]
while True:
    order = input("메뉴 입력 (1.냉면, 2.볶음밥, 3.피자, 4.짜장면, 5.주문취소 (숫자로 입력해 주세요)): ")

    try:
        print(menu[int(order)-1] + '을 선택')
    except ValueError:
        print('숫자만 입력 가능')
        continue
    except IndexError:
        print('없는 메뉴임')
        continue
    else:
        break
    finally:
        i = int(order)
        print('----------------------')
        

if int(order) == 1:
    print('냉면은 여름에')
elif int(order) == 2:
    print('볶음밥은 기름지네')
elif int(order) == 3:
    print('피자는 간식')
elif int(order) == 4:
    print('짜장면은 중식')
elif int(order) == 5:
    print('주문 취소되었음')