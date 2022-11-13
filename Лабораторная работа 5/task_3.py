from random import shuffle
def get_unique_list_numbers() -> list[int]:
    num = range(-10, 11)
    list_unique_numbers = []
    unique_num = set(num)
    for num in unique_num:
        list_unique_numbers.append(num)
    shuffle(list_unique_numbers)
    return list_unique_numbers[:15]

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
