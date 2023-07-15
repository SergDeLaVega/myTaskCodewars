"""
Дон Дрампхет живет в хорошем районе, но один из его соседей начал сдавать свой дом в аренду.
Дон Дрампхет хочет построить стену между своим домом и домом соседа и пытается
заставить ассоциацию соседей заплатить за это. Он начинает уговаривать своих соседей подать петицию,
чтобы заставить ассоциацию построить стену. К несчастью для Дона Драмфета,
он не очень хорошо читает, обладает очень ограниченной концентрацией внимания и может запомнить
только две буквы из имен каждого из своих соседей. Собирая подписи, он настаивает на том,
чтобы его соседи продолжали сокращать свои имена до тех пор, пока не останутся две буквы,
и он, наконец, сможет их прочитать.

Ваш код отобразит полное имя соседа и усеченную версию имени в виде массива.
Если количество символов в имени меньше или равно двум, он вернет массив,
содержащий только имя как есть"
"""
#test.assert_equals(who_is_paying("Mexico"),["Mexico", "Me"])
#test.assert_equals(who_is_paying("Me"),["Me"])
#test.assert_equals(who_is_paying("Me"),["Me"])
#test.assert_equals(who_is_paying(""), [""])
#test.assert_equals(who_is_paying("I"), ["I"])

#Мое решение
def who_is_paying(name):
    nameList = []
    if len(name)>2:
        nameList.append(name)
        nameList.append(name[:2])
    elif len(name)<3 :
        nameList.append(name)
    return nameList

#Не мое решение
def who_is_paying_1(name):
    return [name,name[0:2]] if len(name)>2 else [name]


def who_is_paying_2(name):
    if len(name) > 2:
        return [name, name[0:2]]
    else:
        return [name[0:len(name)]]



print(who_is_paying_1("Al"))





