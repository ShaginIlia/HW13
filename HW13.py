def test(name, age, course=[1, 2, 3, 4], *args):
    print('Ваше имя: ', name)
    print(*args)
    if int(age) < 18:
        return print('Недоступно')
    else:
        print('Ваш возраст:', age, 'лет')
    if course > 4:
        return print('Недоступно')
    else:
        return print('Ваш курс:', course)


test('Ilia', 20, 2, 11, 12, 13)


def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n - 1)


print(rec(7))
