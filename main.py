def get_book_text(filepath):
    """Takes a filepath and returns the contents of the file as a string."""
    with open(filepath) as f:
        return f.read()

def main():
    # Use the relative path to your frankenstein.txt file
    text = get_book_text("books/frankenstein.txt")
    print(text)

# Call main to run program
if __name__ == "__main__":
    main()
