data = int(input())
for i in range(1,data+1):
  i = str(i)
  print_dash = i.count('3')+i.count('6')+i.count('9')
  if print_dash == 0:
    print(i,end=" ")
  else:
    print("-"*print_dash,end=" ")

# 간단한 문자열 판별 후 풀이 / 리스트로도 구현 가능할 것 같다.
