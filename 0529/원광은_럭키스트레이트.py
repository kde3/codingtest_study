'''
럭키스트레이트

현재 캐릭터 점수 n
자릿수를 기준으로 n을 반으로 나누어
왼쪽부분의 각 자릿수 합
오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황

조건)
n의 자릿수는 항상 짝수로 입력된다

입력)
123402
출력)
lucky

입력)
7755
출력)
ready
'''

#n = int(input())
n = 7755
def solution(n):
    tmp1, tmp2 = 0, 0
    strN = str(n)
    print(f"n:{strN}, len:{len(strN)}")

    leftStr = strN[0:int(len(strN)/2)]
    rightStr = strN[int(len(strN)/2):]
    print(leftStr, rightStr)

    for i in leftStr:
        tmp1 += int(i)
    for j in rightStr:
        tmp2 += int(j)

    if tmp1 == tmp2:
        print("lucky")
    else:
        print("ready")
        
    return 
solution(n)