arr = [[1, 2, 3, 10],
       [4, 5, 6, 11],
       [7, 8, 9, 12],
       [13, 14, 15, 16]]

# need = [[10, 3, 2, 1],
#        [11, 6, 5, 4],
#        [12, 9, 8, 7],
#        [16, 15,14,13]]





def p_matrix(arr):
    for i in range(len(arr)):
        for s in range(len(arr[i])):
            print(arr[i][s],  end=' ')

        print()


#p_matrix(arr)


def array_zero(m, n):
    #This functiun creates multidimenshional arrays
    ar = []
    for i in range(m):
        internal_arr = []
        for j in range(n):
            internal_arr.append('Настя ты ')
        ar.append(internal_arr)
    return ar


#print(array_zero(3, 3))
#p_matrix(array_zero(3, 3))

def swap(i, s, j):

    temp = i[s]
    i[s] = i[j]
    i[j] = temp


def mirror(arr):
    for i in arr:
        for s in range(len(i) // 2):
            swap(i, s, len(i) - 1 - s)


print(mirror(arr))
p_matrix(arr)

w = 'fihifhi'
r =11111111
print(id(w))
print(id(r))

list = [2,4,6,8,9]
empty_list = []
comprehension = [num * 3 for num in list]
print(comprehension)


interval = [yum * 3 for yum in range(1, 6)]
print(interval)

inter = []
for ter in range(1, 6):
    inter.append(ter * 3)
print(inter)

nums = [2, 4,7,9,23,45,10]
unt = [d**2 for d in nums if d < 10]
print(unt)

words = ['found', 'love', 'beautiful', 'girl', 'yesterday']
my_words = [wor for wor in words if len(wor) < 6]
print(my_words)

fff = [lll * 2 for lll in range(10, 1, -1)]
print(fff, end=' ')

aaa = [aa*2 for aa in reversed(range(1, 11)) if aa % 2 == 0]
print(aaa)