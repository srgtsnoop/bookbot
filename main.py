from stats import get_num_words, get_characters, short_character_counts


def get_book_text(filepath):
    """Takes a filepath and returns the contents of the file as a string."""
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    
    # Word count
    num_words = get_num_words(text)
    
    # Character count
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        if item["char"].isalpha():   # skip spaces/punctuation/etc
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()