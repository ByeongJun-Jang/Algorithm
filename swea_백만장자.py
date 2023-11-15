case = int(input())

for test in range(1,case+1):
    data_l = int(input())
    data = list(map(int,input().split()))[::-1]
    price=data[0]
    benefit=0

    for i in range(1,len(data)):
      if data[i]>=price:
        price=data[i]
      else :
        benefit += price-data[i]

    print(f"#{test} {benefit}")


# 배열을 역으로 순회해야 풀리는 문제
