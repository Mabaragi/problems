def solution(temperature, t1, t2, a, b, onboard):
    N = len(onboard)
    temperature += 10
    t1 += 10
    t2 += 10
    INF = 10e4
    dp = [[INF] * N for _ in range(51)]
    dp[temperature][0] = 0
    for i in range(N - 1):
        for t in range(51):
            if dp[t][i] == INF:  # 생략
                continue
            for dt in (1, 0, -1):  # 상승, 유지, 하강
                nt = t + dt
                if nt == temperature: dc = 0  # 희망온도가 실외온도와 같은경우에 비용은 0
                elif nt == t: dc = b  # 희망온도가 실외온도와 다르고 희망온도가 현재온도일 경우에 비용 b
                elif t < temperature and dt == 1: dc = 0# 실외온도가 현재온도보다 높고 온도 상승일 경우에 비용 0
                elif t > temperature and dt == -1: dc = 0
                else: dc = a


                if nt < 0 or nt > 50:
                    continue
                if (onboard[i + 1] == 1) and (nt > t2 or nt < t1):  #f 승객이 탑승하고 온도가 범위 밖일 경우에 생략
                    continue
                dp[nt][i + 1] = min(dp[nt][i + 1], dp[t][i] + dc)

    answer = min(dp[i][-1] for i in range(51))
    return answer