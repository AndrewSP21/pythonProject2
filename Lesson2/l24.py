# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

lis = input('Введите список слов через пробел: ').split()
count = 1
for v in lis:
    print(count, ': ', v[:10])
    count += 1


for idx, word in enumerate(lis):
    print(f'{idx}:{word[:10]}')