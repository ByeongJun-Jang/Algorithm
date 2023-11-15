data = input()
test = []
answer = 0
for i in range(len(data)):
  if len(data) == 0:
    test.append(i)
  elif test[-1] == data[i]:
    test.pop()
  else :
    test.append()

if len(data) == 0:
  answer = 1

print(answer)
