# a = set()
# list_num = [1, 3,1, 2,2,3,3,4,5,5,7,7,6,6,43,4, 4, 5, 7, 6, 5, 43, 4]
# [a.add(i) for i in list_num]
# print(a)
# print(sum(a))

# list_num = [1, 3,1, 2,2,3,3,4,5,5,7,7,6,6,43,4, 4, 5, 7, 6, 5, 43, 4]
# print(sum(set(list_num)))

def func(my_set, my_list):
    if len(my_set) < len(my_list):
        return False
    for el in my_list:
        if el in my_set:
            continue
        else:
            return False
    return True


print(func({3,4,5,6,56,8,12}, [3,4,3,4,4,4,4,4,4,4,4,4,4,4]))
