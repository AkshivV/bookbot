def count_words(book_txt):
    return len(book_txt.split())

def count_occurrence(book_txt):
    char_counts = {}
    for word in book_txt.split():
        for char in list(word):
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts