# a = [1, 2, 3, 4, 5, 6]
# b = []
# #c = [i*2 for i in a]
# d = [b.append(i**5) for i in a]
# #print(c)
# print(b)

# a = [1, 12, 23, 45, 6, 7, 8, 9, 13]
# b = []
# [b.append(i**2) for i in a if i < 23]
# print(b)
#
# a = ['asterix', 'obelix', 'master', 'develop', 'senior', 'jun']
# print([w for w in a if len(w) < 9])

# print([i*2 for i in range(10, 1, -1) if i % 2 == 0])
a = ['asterix', 'obelix', 'master', 'develop', 'senior', 'jun']
print([w.ljust(len(w)+1, '.') for w in a if len(w) < 7])
print([w + '.' for w in a if len(w) < 7])
