# # 주어진 금액에 맞게 최소한의 동전을 제공하는 문제
# # N = 주어진 금액 arr = 동전의 종류별 가격

N = int(input())
arr = [10, 50, 100, 500]

def solution(N, arr):
  arr.reverse()
  count = 0  # 카운트될 변수

  for coin in arr:
    while N >= coin: # 주어진 금액이 현재로써 가장 큰 코인보다 클경우에 반복문 실행
      N -= coin
      count += 1
    # while문이 끝나면 coin이 한단계 낮은 금액으로 바뀐다.
  return count

print(solution(N, arr))
