def delete(list_, index=None):
    result = [] # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
         index = len(list_) - 1
    for i in range(len(list_)):
        if i != index:
            result.append(list_[i])

    return result



print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
