def get_book_text(path):

    with open(path) as f:
        return f.read()

def get_num_words(text):

    words = text.split()
    return len(words)       

def main():

    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(f"{num_words} in the document")

    

if __name__ == "__main__":
    main()