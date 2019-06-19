# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
sum = 0
list = []
for i in range(5):
    inputNum = input('list[] >> ')
    list.append(int(inputNum))

for i in list:
    sum += i
print('평균',sum/5)