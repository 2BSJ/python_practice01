# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

list = [1, 2, 3, 4, 5, 6, 7]
count = 0
sum = 0
for i in range(0, len(list)):
    if list[i] % 3 == 0:
        sum += list[i]
        count += 1

print('주어진 리스트에서 3의 배수의 개수 =>',count)
print('주어진 리스트에서 3의 배수의 합 =>',sum)
