# 점화식, 재귀함수을 통해 구하는 문제
# 계단을 1칸 혹은 2칸씩 올라가는 경우가 있다고 했을 때 n 번쨰 계단에
# 도달할 수 있는 총 경우의 수는 몇개인가?

def dfs(k):
    if dy[k] > 0:
        return dy[k]
    if k == 1 or k == 2:
        return k
    else :
        dy[k] = dfs(k - 1) + dfs(k - 2)
        return dy[k]
N = int(input())
dy = [0] * (N + 1)

print(dfs(N))