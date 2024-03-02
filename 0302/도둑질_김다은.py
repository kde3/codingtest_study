def solution(money):
    
    dp1 = []
    dp1.append(money[0])
    dp1.append(money[1])
    dp1.append(dp1[0] + money[2])

    dp2 = []
    dp2.append(0)
    dp2.append(money[1])
    dp2.append(dp2[0] + money[2])

    # 1. 첫 번째 집을 턴다(마지막 집은 X).
    for i in range(3, len(money)-1) :
        dp1.append(max(dp1[i-2], dp1[i-3]) + money[i])
    case1 = max(dp1[-1], dp1[-2])

    # 2. 마지막 집을 턴다.
    for i in range(3, len(money)) :
        dp2.append(max(dp2[i-2], dp2[i-3]) + money[i])
    case2 = max(dp2[-1], dp2[-2])

    return max(case1, case2)