# main.py
import sys
from stats import get_num_words, get_characters, sort_character_counts

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    # Require exactly one argument: the path to the book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    # Word count
    num_words = get_num_words(text)

    # Character counts and sort by frequency
    char_counts = get_characters(text)
    sorted_chars = sort_character_counts(char_counts)

    # Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():  # skip non-alphabetical characters
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
