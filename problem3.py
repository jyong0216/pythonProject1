a = int(input("숫자를 입력하세요 : "))
result = 1
for item in range(1, a+1):
    result *= item
print(result)