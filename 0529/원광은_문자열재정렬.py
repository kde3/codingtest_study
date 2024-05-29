'''
문자열 재정렬

알파벳 대문자와 숫자(0~9)로만 구성된 문자열 입력

모든 알파벳 오름차순으로 정렬해 이어서 출력한 뒤
모든 숫자를 더한 값을 이어서 출력

입력)
K1KA5CB7
출력)
ABCKK13

입력)
AJKDLSI412K4JSJ9D
출력)
ADDIJJJKKLSS20
'''

#n = input()
n = "AJKDLSI412K4JSJ9D"
def solution(n):
    tmpStr = []   # 문자
    tmpNum = 0    # 숫자
    for i in n:
        if i.isalpha():    # 알파벳이면
            tmpStr.append(i)
        else:
            tmpNum += int(i)
    tmpStr.sort()          # 문자기준 오름차순 정렬
    tmpStr.append(str(tmpNum))
    
    print("".join(tmpStr))
            
    return 

solution(n)
