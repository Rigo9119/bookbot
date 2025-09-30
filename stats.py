def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def words_counter(book):
    words = len(book.split())
    return words

def chars_counter(book):
    chars = book.lower()
    chars_dic = {}
    for char in chars:
        if char in chars_dic:
            chars_dic[char] += 1
        else:
            chars_dic[char] = 1
    return chars_dic

def sort_on(items):
    return items["num"]

def sorted_chars_dicts(chars):
    dicts_list = []

    for char, count in chars.items():
        if char.isalpha():
            dicts_list.append({"char": char, "num": count})

    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list
