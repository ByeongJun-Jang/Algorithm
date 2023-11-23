data = int(input())
answer = 0
for i in range(1,data+1):
  sum=0
  for k in range(i,data+1):
    sum += k
    if sum == data:
      answer += 1
    elif sum > data:
      break

answer
# 완전 탐색을 활용하여 풀어야 하는 문제

def solution(data):
  answer=0
  for i in range(1,data+1):
    sum = 0
    for k in range(i,data+1):
      sum += k
      if sum == data:
        answer += 1
      elif sum > data:
        break

  return data
