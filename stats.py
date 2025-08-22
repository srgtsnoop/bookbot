def get_num_words(text):
    """Takes a string and returns the number of words in it."""
    words = text.split()
    return len(words)

def get_characters(text):
    count = {}
    for characters in text.lower():
        if characters in count:
            count[characters] += 1
        else:
            count[characters] = 1
    return count


def short_character_counts(char_counts):
    sorted_list = [{"char": char, "num": count} for characters, count in char_counts.items()]
    
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list

