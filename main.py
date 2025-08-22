def get_book_text(filepath):
    """Takes a filepath and returns the contents of the file as a string."""
    with open(filepath) as f:
        return f.read()

def get_num_words(text):
    """Takes a string and returns the number of words in it."""
    words = text.split()
    return len(words)

def main():
    # Use the relative path to your frankenstein.txt file
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

# Call main to run program
if __name__ == "__main__":
    main()
