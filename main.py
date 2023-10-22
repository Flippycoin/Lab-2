import csv

f = open('result.txt', 'w')
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    z = -1
    title = 0
    author = input('Введите желаемого автора: ')
    search = input('Введите 1, если хотите ввести 20 ID книг для библиографической ссылки, иначе введите 0 для случайного набора ')
    id_array = []
    tags_array = []
    flag = 0
    bible = 20
    numbers = []
    # задание 4 часть 1
    if search == '1':
        for i in range(bible):
            id_array.append(input('Введите ID искомой книги '))
    else:
        flag = 1

    for row in books:
        # задание 1
        z += 1
        # задание 2
        if len(row[1]) > 30:
            title += 1

        # задание 3
        year = row[6].split()
        year = year[0].split('.')
        year = year[-1]

        surname = row[3].split()
        surname = surname[-1:]
        if len(surname) > 0:
            if (author == str(surname[0])) and (int(year) == 2015 or int(year) == 2018):
                print(row[1])

        # задание 4 часть 2
        if flag == 0:
            if row[0] in id_array:
                f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')
        elif (flag == 1) and (z < 22) and (z > 1):
            f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')

        if z > 0:
            numbers.append(int(row[8]))

        # доп задание 1
        tags = row[12].split('#')
        for tag in tags:
            if not (tag in tags_array):
                tags_array.append(tag)

    print('Всего записей:', z)
    print('Количество записей длиной > 30:', title)
    tags_array.pop(0)
    tags_array.pop(0)
    print('Перечень всех тегов: ', tags_array)

    # Доп задание 2
    print('Самые популярные 20 книг:')
    numbers.sort(reverse=True)
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    z = -1
    m = 0
    books_array = []
    for row in books:
        z += 1
        book = row[1]
        if (z > 0) and (int(row[8]) == numbers[m]) and (m < 20) and not (book in books_array):
            books_array.append(book)
            print(row[1])
            m += 1

f.close()
