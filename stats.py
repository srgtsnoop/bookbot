def get_num_words(text):
    """Takes a string and returns the number of words in it."""
    words = text.split()
    return len(words)

def get_characters(text):
    """Counts all characters in the text (case-insensitive)."""
    count = {}
    for char in text.lower():   # use singular "char" for clarity
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_character_counts(char_counts):
    """Takes a dict of char counts and returns a sorted list of dicts."""
    # Convert dict -> list of {"char": x, "num": y}
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    
    # Sort by num descending
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list
