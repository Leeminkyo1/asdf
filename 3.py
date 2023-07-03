def menu():
    print('1. 명함입력')
    print('2. 명함검색(이름)')
    print('3. 명함전체출력')
    print('4. 자료 수정')
    print('5. 자료 일부 삭제')
    print('6. 전체 삭제')
    print('7. 종료')
    x = input('메뉴를 선택하세요 : ')
    return x
def insert():
    data1 = [0, 0, 0, 0]
    data1[0] = input('이름 입력 :')
    data1[1] = input('전화번호 입력 :')
    data1[2] = input('직장 입력 :')
    data1[3] = input('직급 입력 :')
    return data1
#프로그램 실행영역
lst = []
import re
while 1:
    choice = menu()
    if None==(re.match("[1-7]", choice)):  #메뉴 번호 없는 것 입력 시 메뉴 화면 루프
        print("잘못선택하였습니다.")
        continue
    if choice =='1':
        lst.append(insert())
    elif choice =='2':
        name = input('찾는 명함 이름 혹은 번호 입력 :')
        for i in lst:
            if i[0] == name or i[1] == name:
                print(i)
    elif choice =='3':
        for i in lst:
            print(i)
    elif choice =='4':
        name = input('변경할 이름 혹은 번호 입력 :')
        for i in lst:
            if i[0] == name or i[1] == name:
                i[0] = input("이름 변경 : ")
                i[1] = input("전화번호변경 : ") 
    elif choice =='5':
        name = input('삭제할 명함 혹은 번호 입력 :')
        for i in range(len(lst)):
            if lst[i][0] == name or lst[i][1] == name:
                lst.pop(i)
                print("삭제성공하였습니다.")
                break       
    elif choice =='6':
        lst = []    
    elif choice =='7':
        print('프로그램 종료.')
        obj = open("data.txt",'w')
        for i in lst:
            obj.write("%s,%s,%s,%s"%(i[0],i[1],i[2],i[3]))
        
                
        obj.close()
        break
    else :
        print('잘못 선택\n')











