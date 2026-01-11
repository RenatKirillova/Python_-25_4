# TODO реализовать функцию
def remove_whitespace(text):
    while "  " in text:
        text = text.replace("  ", " ")
    return text

str_with_space = """123.    test bks
print   test11"""

print(remove_whitespace(str_with_space))
