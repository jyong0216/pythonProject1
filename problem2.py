i = 0
sum = 0
N = int(input("슛자를 입력하세요:"))
for i in range(1,N+1):
    if i % 2 == 0:
        sum = sum + i
    else:
        pass

print("1부터 N까지의 합은: {}".format(sum))