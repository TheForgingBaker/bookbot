# To handle book stats

def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return f"{word_count} words found in the document"


def get_chars_count(text):
    chars = {}
    for character in text:
        lowered = character.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
