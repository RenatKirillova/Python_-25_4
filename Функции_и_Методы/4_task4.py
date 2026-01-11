# TODO реализовать функцию
def insert(intens, value, index=0):
    result = []
    for i in range(len(intens)):
        if i == index:
            result.append(value)
        result.append(intens[i])


    if index >= len(intens):
        result.append(value)
    return result


print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]

