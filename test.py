import random as rd


print("가위 바위 보")


while True:
    try:
        com = rd.choice([0, 1, 2])
        a = input("가위 바위 보 입력 : ")
        
        if a == '가위':
            a = 0
        elif a == '바위':
            a = 1
        elif a == '보':
            a = 2 

        if com == a:
            print('무승부')
        elif com > a: 
            print('패배')
        elif com < a:
            print('승리')
            break

    except Exception as e:
        print(e)
        

