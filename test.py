# список, кортеж, словарь и множество

# !! Список(массив) - упорядоченный набор данных
# shoplist = ['1', '2', '3', '4']

# !! Кортеж(аналог массива - но неизменяемый)
# zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обязательны

# zoo = '1', '2', '3'
# zoo2 = 'a', 'b', 'c', zoo
# print(zoo2[3][2])

# !! Словарь -  (объект)
# ab = {'a': 22, 'b': '11'}
# print(ab['a'])

# !! Множество (set) - неупорядоченные наборы простых объектов
# bri = set(['Бразилия', 'Россия', 'Индия'])


a = {(3,4), (1,2), (5,7)}
a.add((5, 12))

for num in a:
    print(num[1])

# print()
if(3,4) in a:
    print(a)


def is_valid_position(x, y):
    if not (0 <= x < 6 and 0 <= y < 6):
        return False
    # for ship in self.ships:
    #     for sx, sy in ship.positions:
    #         if abs(x - sx) <= 1 and abs(y - sy) <= 1:
    #             return False
    return True

print(is_valid_position(1, 22))

class Ship:
    def __init__(self, positions):
        self.positions = positions  # ?? массив [(x,y), (x,y)] - в зависимости какой длины корабль
        self.hits = []   # список - массив [(x, y), (x, y)]

bb = Ship({(2,3)})
# bb.positions.
print(bb.positions)