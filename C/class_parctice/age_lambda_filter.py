ages = [14, 56, 57, 82, 32, 18]

print('성년 리스트 : ')
for a in filter(lambda x: x >= 19, ages):
    print(a, end = ' ')
