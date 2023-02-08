ab = ['first', 1, 2, 3, 'second', 10, 20, 30, 'third', 100, 200, 300, 'fourth', -50]
my_dict = {}
ek = None
for i in ab:
    if type(i) == str:
        my_dict[i] = []
        ek = i
        # print(ek)

    else:
        my_dict[ek].append(i)


# print(my_dict)

#print(hash((1,2,3,4,5,6,7)))


def far ():
    def hello():
        print("junior")

        def bbay():
            print('Dedlay')

    print('jungo')


my_text = "Он несет спасенье несет тем сердцам тем что сердцам верят Он спасенье"
# print(my_text.split('тем'))
new_dict = {}
for word in my_text.split():
    if word in new_dict:
        new_dict[word] = new_dict[word] + 1
    else:
        new_dict[word] = 1
# print(new_dict)

new_dict1 ={}
for w in my_text.split():
    new_dict1[w] = new_dict1.get(w, 0) + 1

# print(new_dict1)
asd = [1,3,5,7,8,9]
sa = ['sfd','dkjh', 'jashd']
d =[asd,
    [3,4,5,6],
    asd, sa,
    ['djdf', 'dfs',[[2,3,4,['fffffff',4,5,6],6],3,4,'jsdhgf'],44,4,0]]
for i in d:
    for t in i:
        print(t, end="  ")



# print(d[4][2][0][3][0])


