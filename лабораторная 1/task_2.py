# TODO Найдите количество книг, которое можно разместить на дискете
lists = 100
value = 1.44 * 1024*1024
stroki = 50
simv = 25
amount = value / (4 * lists * stroki * simv)
print("Количество книг, помещающихся на дискету:", round(amount))