def get_num_words(text):  # Renamed to avoid conflict
    word_list = text.split()
    num_words = len(word_list)
    word_string = f"{num_words} words found in the document"
    return word_string