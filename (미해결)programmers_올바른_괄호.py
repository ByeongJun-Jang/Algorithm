def solution(data):
  if data.count('(') != data.count(')'):
    return False
  test=[]
  for i in data:
    if i == '(':
      test.append(data[i])
    if i == ')':
      if data[0] == (')'):
        return False
        if len(test) == 0:
          return False
        else :
          test.pop()
    
  return True

  # 정확성: 54.1 효율성: 30.5 합계: 84.6 / 100.0  이 도출이 됨 다시 고민할 필요가 있음
