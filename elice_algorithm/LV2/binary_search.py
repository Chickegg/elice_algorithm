# 이분 탐색을 통해서 카운터별 처리속도를 통해 최단시간의 결과값을 도출해 내는 문제

def solution(n, times):
  times.sort() # 오름차순으로 정렬
  left = (times[0] * n) // len(times)  #최소경우
  right = times[-1] * n # 최대경우

  while left < right : #최소값이 최대값보다 작은경우
    mid = (left + right) // 2 
    temp = 0

    for time in times:
      temp += mid // time
    if n <= temp: # 시간이 남는 경우?
      right = mid # 큰 값을 중간값으로 대체한다.
    else: # 시간이 부족한 경우?
      left = mid + 1 # 작은값은 중간값의 다음 값이다.
  return right # while문이 끝나면 최댓값이 정답이 된다.

N = int(input())
times = list(map(int, input().split()))

print(solution(N, times))
    