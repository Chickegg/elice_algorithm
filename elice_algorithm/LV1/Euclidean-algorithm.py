# 일정한 간격을 두고 가로등을 배치하고 싶을 때 
# 유클리드 호제법을 사용하여 최대공약수를 구해 완전한 상태의 가로등배열을 구현하고
# 현재 가로등 배열과 비교하여 필요한 가로등의 갯수를 구한다.

arr = list(map(int, input().split()))

GCDarr = arr[0] # 최대공약수의 초깃값

def GCD(a, b):
  while b != 0: # 뒤의 수가 0이 아닐 경우
    a, b = b, a % b # a는 뒤의 숫자가 오게되고 b에는 최대공약수를 b로 나누었을때의 나머지가 오게된다.
    # 더 이상 뒤의수를 통해 값의 변화가 없을 경우
  return a # 현재까지 구해진 최대공약수를 a라고하고 반환한다.

# GCD함수를 배열의 모든 요소를 대상으로 실행시켜준다.
for i in range(len(arr)):
  GCDarr = GCD(GCDarr, arr[i]) # 최대공약수는 현재 최대공약수와 배열의 다음 요소를 입력인자로 한 함수로 결정된다.

resultArr = [] 
# 최종 결과 배열을 구현하는 부분
for i in range(arr[0], arr[-1] + GCDarr, GCDarr):
  resultArr.append(i)

resultArrSet = set(resultArr)
arrSet = set(arr)

answer = len(resultArrSet.difference(arrSet))
print(answer)



