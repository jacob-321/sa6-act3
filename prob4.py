num_list1 = [1,2,3]

num_list2 = [1,2,3,4,5,6,7,8,9]

intersect = list(filter(lambda x: x in num_list1, num_list2))

print(intersect)