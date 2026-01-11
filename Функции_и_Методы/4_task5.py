# TODO реализовать функцию
def get_sentences_list(text):
    result = []

    parts = text.split(".")
    for part in parts:
        sentence = part.strip()
        if sentence != "":
            result.append(sentence)
    return result
    ...


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))

