import random

res = []  #점수들
maxnum = 0 #최고기록

while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임시작 2.기록확인 3.게임종료")
    menu = int(input()) # 메뉴에서 입력받음 어떤 걸 진행할지

    if(menu == 1): # 게임시작을 눌렀을 때
        ans = random.randint(1,101) ##랜덤으로 게임에서 지정해줌
        l = 1 #왼쪽값
        r=100 #오른쪽값
        i=0	#몇번째 도전인지

        while True:
            i+=1
            if(i > 10):
                print("게임오버") #최대 기회는 10번으로 지정한다.
                break

            print("%d번째 숫자 입력(%d~%d)" % (i,l,r)) #몇번째 입력한건지 , 범위와 함께 알려줌
            num = int(input(""))
            if(num < ans): #입력값이 정답보다 작을때에 출력
                print("UP")
                l = num
            elif(num > ans):
                print("DOWN")
                r = num
            else:
                print("정답\n%d번만에 맞춤" % i)
                if(maxnum < i): #여태 맞춘 기록보다 짧으면 최고 기록을 갱신해준다
                    print("최고 기록 갱신~!")
                    maxnum = i
                res.append(i) #몇번에 맞춘건지 기록해준다
                break
    elif(menu == 2): # 기록보기를 선택했을때
        res.sort() #점수 정렬
        for i in range(len(res)):
            print("%d. %d" % (i+1,res[i]))
    else: # 게임 종료를 눌렀을때
        break
