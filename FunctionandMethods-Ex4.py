 def unique_list(lst):
    return list(set(lst))
unique_list ([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def unique_list(lst):
    seen_numbers=[]
    for nb in lst:
        if nb not in seen_numbers:
            seen_numbers.append(nb)
    return seen_numbers

unique_list ([1,1,1,1,2,2,3,3,3,3,4,5])

