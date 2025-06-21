from stats import get_word_count
from stats import get_chars_count


def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(get_word_count(book_text))
    print(get_chars_count(book_text))


main()
