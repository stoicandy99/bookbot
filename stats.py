def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def split_into_words(text):
    return text.split()

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(dict_item):
    return dict_item["num"]

def sort_character_counts(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list