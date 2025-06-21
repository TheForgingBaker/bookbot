def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return f"{word_count} words found in the document"


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(get_word_count(book_text))


main()
