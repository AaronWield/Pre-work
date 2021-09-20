def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [1,2,3,4,6]
print(is_consecutive(a_list))
