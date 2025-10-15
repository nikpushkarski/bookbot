def count_words(text):
    all_words = text.split(sep=None)
    return len(all_words)

def count_letters(text):
    letters_dict = {}
    for letter in text.lower():
        if letter.isalpha():
            letters_dict[letter] = letters_dict.get(letter, 0) + 1
    return letters_dict

def sort_on(items):
    return items["num"]

def sorted_letters(letters_dict):
    letters_num_list = []
    for key in letters_dict:
        char_dict = {}
        char_dict["char"] = key
        char_dict["num"] = letters_dict[key]
        letters_num_list.append(char_dict)
    letters_num_list.sort(reverse=True, key=sort_on)
    return letters_num_list
