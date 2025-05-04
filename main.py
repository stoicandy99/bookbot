from stats import get_num_words, char_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    num_words_string = get_num_words(book_text)
    print(num_words_string)
    char_dict = char_dictionary(book_text)
    print(char_dict)
main()
