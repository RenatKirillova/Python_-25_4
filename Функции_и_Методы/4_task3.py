# TODO реализовать функцию count
def count(items, value):
    result = 0
    for item in items:
        if item == value:
            result += 1
    return result

list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True

