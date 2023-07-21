"""
Учитывая число n, нарисуйте лестницу,
используя букву "I", n в высоту и n в ширину,
с самой высокой в левом верхнем углу.

Например, n = 3 приводит к: "I\n I\n  I"
"""
def draw_stairs(n):
    rez = ""
    i=1
    while i<n:
        rez += "I\n" + " "*i
        i+=1
    rez+="I"
    return rez


print(draw_stairs(3))

def draw_stairs_1(n):
    for i in range(0, n):
        print(" " * i +"I")

def draw_stairs_2(n):
    return '\n'.join(' '*i+'I' for i in range(n))


def draw_stairs_3(n):
    count = 1
    res = ""
    while count < n:
        res += "I\n" + " " * count
        count += 1
    res += "I"
    return res



