def get_num_words(text):  # Renamed to avoid conflict
    word_list = text.split()
    num_words = len(word_list)
    word_string = f"{num_words} words found in the document"
    return word_string

def char_dictionary(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

