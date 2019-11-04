def check_kion(x, y, z):
    return "{0}時の{1}は{2}".format(x, y, z)


time = 12
word = "気温"
do = 22.4
print(check_kion(time, word, do))
