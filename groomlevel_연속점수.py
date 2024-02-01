'''
i 부터 i-1보다 1 크면 누적
i-1보다 1 큰게 아니면 누적하지말고 s[i]초기화
'''
num = int(input())
score = list(map(int, input().split(" ")))
def solution(num,score):
  start = score[0]
  sum = score[0]
  maxx = score[0]
  for c in score[1:] :
    if c-start == 1:
      sum += c
    else:
      sum = c
    
    maxx = max(maxx,sum)
    start = c
  
  return maxx

print(solution(num,score))
