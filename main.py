def get_books_test(path):
    filecontents = ""
    with open(path) as f:
        filecontents = f.read()
    return filecontents

def count_words(book_txt):
    return len(book_txt.split())

def main():
    num = count_words(get_books_test("books/frankenstein.txt"))
    print(f"{num} words found in the document")

main()