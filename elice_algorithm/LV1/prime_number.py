N = int(input())

# 소수를 구하기에 적합한 에라토스테네스의 체를 사용하였다.
# 에라토스테네스의 체를 사용하면  주어진 수 N의 제곱근 까지만 탐색할 수 있다.

# primeNumber를 구하는 함수
def prime_list(n):
  seive = [False, False] + [True] * (N - 1)
  m = int(n ** 0.5)

  for i in range(2, m + 1): # 2부터 N의 제곱근 m까지 탐색
    if seive[i] == True:
      for j in range(i + i, N + 1, i): # i+i의 배수들을 False로 지정
        seive[j] == False
  return [i for i in range(2, N + 1) if seive[i] == True]

print(prime_list(N))
