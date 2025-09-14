list = [1,6,3,4,5,116,7,8,12,115,'a','n','h','d','e','b','g','i','l','v']

list_str = [x for x in list if isinstance(x, str)]
list_int = [x for x in list if isinstance(x, int)]
list_int.sort()
list_str.sort()

list_sort = list_int.copy()
list_sort.extend(list_str)

list_2 = []

for n in list_int:
    if n % 2 == 0:
        list_2.append(n)

list_STR = []

for x in list_str:
    list_STR.append(x.upper())

print('Початковий список:',list)
print('Сортований список:',list_sort)
print('Список кратних 2:',list_2)
print('Список капсом:',list_STR)