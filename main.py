import sys
from stats import (count_words, 
                  count_letters,
                  sorted_letters)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    letters_dict = count_letters(text)

    letters_desc = sorted_letters(letters_dict)
    for pair in letters_desc:
        print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")

main()