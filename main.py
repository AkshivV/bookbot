from stats import count_words
from stats import count_occurrence
from stats import dict_to_sorted_list

def get_books_test(path):
    filecontents = ""
    with open(path) as f:
        filecontents = f.read()
    return filecontents

def sort_on(items):
    return items["num"]

def main():
    path = "books/frankenstein.txt"
    text = get_books_test(path)
    num = count_words(text)
    chars_dict = count_occurrence(text)
    char_list = dict_to_sorted_list(chars_dict)
    char_list.sort(reverse=True, key=sort_on)

    print(f"============ BOOKBOT ============\n Analyzing book found at {path}...\n----------- Word Count ----------\nFound {num} total words\n--------- Character Count -------")
    for char_stat in char_list:
        print(f"{char_stat['char']}: {char_stat['num']}")

    print("============= END ===============")
main()