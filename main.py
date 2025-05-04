from stats import get_book_text, split_into_words, count_characters, sort_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_text = get_book_text(path)

    # Word count
    words = split_into_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")

    # Character count
    char_counts = count_characters(book_text)
    sorted_chars = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
        

main()
