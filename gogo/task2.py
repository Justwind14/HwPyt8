from random import randint, uniform, choice


list_of_weight = ['bryndas', 'sepulchres',
                  'crabs', 'meteorites', 'bulk', 'asteroids']


def main(some_list):
    count_rockets = int(input())
    words = input().split()
    weight = input().split()
    weight[0], weight[1] = int(weight[0]), int(weight[1])
    range_to = input().split()
    range_to[0], range_to[1] = (round(float(range_to[0]), 1), round(float(range_to[1]), 1))
    result_list1 = set()
    result_list2 = set()
    result_list3 = set()
    result_list4 = set()
    while len(result_list1) < count_rockets:
        result_list1.add(str(random_g(words[0], words[1])).replace(']', '').replace("'", "").replace('[', '') + str(randint(10, 99)))
    while len(result_list2) < count_rockets:
        result_list2.add(str(random_g(weight[0], weight[1])).replace(']', '').replace('', "").replace('[', ''))
    while len(result_list3) < count_rockets:
        result_list3.add(str(random_g(range_to[0], range_to[1])).replace(']', '').replace('', "").replace('[', ''))
    while len(result_list4) < count_rockets:
        result_list4.add(random_g(list_of_weight))
        
    res_list = list(zip(result_list1, result_list2,
                    result_list3, result_list4))
    print(res_list)
    return (res_list)


def random_g(x, y=None):
    if type(x) == str and type(y) == str:
        a = list(chr(randint(ord('s'), ord('y'))))
        return a
    if type(x) == int and type(y) == int:
        a = round((randint(x, y))*2, -2)//2
        if x < a < y:
            return a
    if type(x) == float and type(y) == float:
        a = round(uniform(x, y), 1)
        return a
    if type(x) == list and y == None:
        return choice(x)


def print_rocket(ls: list):
    for i in ls:
        print(f'Roket {i[0]} ({i[1]}, {i[2]}) follows with cargo of {i[3]}')

print_rocket(main(list_of_weight))