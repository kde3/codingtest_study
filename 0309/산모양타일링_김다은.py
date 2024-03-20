def solution(n, tops):

    dp = [0] * (2*n+1)

    dp[0] = 1
    dp[1] = 2 + tops[0]
    dp[2] = dp[0] + dp[1]

    #3부터 시작
    for i in range(1, n) :
        #역방향
        if tops[i] == 1 :
            dp[2*i+1] = (dp[2*i] * 2 + dp[2*i-1])%10007
        else :
            dp[2*i+1] = (dp[2*i] + dp[2*i-1])%10007

        #정방향
        dp[2*i+2] = (dp[2*i+1] + dp[2*i])%10007

    return dp[-1]