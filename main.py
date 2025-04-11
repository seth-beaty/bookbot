from stats import count_chars, get_book_report, get_book_text, get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # book_path = "books/frankenstein.txt"
    text = get_book_text(sys.argv[1])
    characters = count_chars(text)
    get_book_report(sys.argv[1], characters)

    

if __name__ == "__main__":
    main()