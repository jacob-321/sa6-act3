num_list = [1,2,3,4,5,6,7,8,9]

maximum = num_list[0]

for x in num_list:
    if x > maximum:
        maximum = x

max_num = (num_list, lambda x, y: x if x > y else y)

print(max_num)