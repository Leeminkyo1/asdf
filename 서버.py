def menu():
    print("1.정보 입력")
    print("2.정보검색")
    print("3.정보 전체 출력")
    print("4.정보 출력")
    print("5.정보 수정")
    print("6.정보 일부 삭제")
    print("7.종료")
    x = input('메뉴을 선택하세요:')
    return x
def insert():
    data1 = [0,0,0,0]
    data1[0] = input('이름 입력:')
    data1[1] = input("전화번호 입력:")
    data1[2] = input('회사 입력:')
    data1[3] = input('직급 입력:')
    return data1
lst = []
import re
while 1:
    choice = menu()
    if None == (re.match("[1-7]", choice)):
        print("잘못선택하였습니다.")
        continue
    if choice == '1':
        lst.append(insert())
    elif choice == '2':
        name = input('찾고자하는 이름을 입력해주세요:')
        for i in lst:
            if i[0] == name or i[1] == name:
                print(i)
    elif choice == '3':
        for i in lst:
            print(i)
    elif choice == '4':
        name = input('변경할 이름을 입력해주세요:')
        for i in lst:
            if i[0] == name or i[1] == name:
                i[1] = input('전화번호:')
                i[2] = input('회사')
                i[3] = input('직급')
    elif choice == '5':
        name = input('삭제할 번호을 입력해주세요:')
        for i in range(len(lst)):
            if lst[i][0] == name or lst[i][1] == name:
                lst.pop(i)
                print('삭제')
                break
    elif choice == '6':
        lst = []
    elif choice == '7':
        print('종료')
        obj = open("data.txt",'w')
        for i in lst:
            obj.write("%s,%s,%s,%s/n"%(i[0].i[1],i[2],i[3]))
        obj.close()
        break
    else:
        print('잘가')


    
    
    
