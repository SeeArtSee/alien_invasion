
my_list = [8, 7, 5, 4, 2, 1, -2, -4, -6, -8, -3]
total = 0
i1 = 0
# while my_list[i1-1] < 0:
#     total = total + my_list[i1-1]
#     i1 -= 1

# print(total)
# print(i1)
for i in my_list:
    if i < 0 or i == 8:
        total = total + i
        i1 += 1
# print(total)
# print(i1)

my_word = ['Волчий',  'вой', 'да', 'лай', 'собак', 'Крепко', 'до', 'боли', 'сжатый', 'кулак']
# a1 = -1
# for a in my_word:
#     if a == 'до':
#        break
#    print(a)
# while my_word[a1] != 'до':
#     a1 = a1 + 1
#     if my_word[a1] == 'до':
#         break
#     print(my_word[a1])

#for s in range(len(my_word)):
#    for d in range(s + 1):
#       print(my_word[s])

my_dict = {}
my_list_keys = []
my_list_values = []
ab = ['first', 1, 2, 3, 'second', 10, 20, 30, 'third', 100, 200, 300, 'fourth', -50]
for k in ab:
    if type(k) == str:
        my_list_keys.append(k)

    else:
        my_list_values.append(k)
        my_dict = dict(zip(my_list_keys, my_list_values))
# print(my_list_keys)
# print(my_list_values)
print(my_dict)
# print(len(ab))

a = ['first', 1, 2, 3, 'second', 10, 20, 'third', 44, 543, 333,'fourth', -50]
d = {}
e = {}
b = []
for i in range(len(a)-1, -1, -1):
    if type(a[i]) == int:
        b.append(a[i])

    else:
        d[a[i]] = b[::-1]
        b = []

c = list(d)[::-1]
for i in range(len(c)):
    e[c[i]] = d[c[i]]
print(e)


lst = ['first', 1, 2, 3, 'second', 4, 5, 'third', 3, 1, 5]
myDict = dict()
values = []
for elem in lst:
    while not type(elem) == str:
        values.append(elem)
        break
    if type(elem) == str:
        values = []
        myDict[elem] = values
print(myDict)

a = ["first", 1, 2, 3,5,9, "second", 10, 20,6, "third", 5, 56, 70, "fourth", -54,6]
d = {}
m = []
x = len(a)
for i in a:
    if type(i) == str:
        b = i
        m.clear()
    if type(i) == int:
        m.append(i)
        d[b] = m[:x]
print(d)

