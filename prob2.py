sort_list = ["ubuntu", "github", "python", "computer", "git"]

sort_order = sorted(sort_list, key=lambda x: (len(x), x))

print(sort_order)