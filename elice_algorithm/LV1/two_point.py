# 투포인트와 슬라이딩 윈도우를 혼합한 문제 주로 투포인트가 사용
# M = 정해진 값 arr = 물건들의 가격이 나열되어져있는 배열
# 연결된 구간중 M의 값을 만족시키는 구간이 존재하는지 탐색하는 문제

M = int(input())
arr = list(map(int, input().split()))

start = end = total = 0
answer = 0

while True:
  if total > M: # 총 값이 주어진 금액보다 크다면?
    total -= arr[start]
    start += 1 # 레프트 포인트를 한칸 오른쪽으로 이동시킨다.
  elif end == len(arr): # 우측포인트가 끝까지 도달했다면
    break #더 이상의 탐색은 무의미하다.
  else: # 아직 금액에 모지라고 우측포인트가 끝점이 아니라면?
    total += arr[end]
    end += 1
  if total == M: # 정확한 값의 구간이 존재한다면?
    answer += 1

if answer >= 1: # 정답구간이 한 구간 이상 존재한다면
  print("여기만큼 계산해 주세요!")
else :
  print("좀 더 둘러보고 오겠습니다.")