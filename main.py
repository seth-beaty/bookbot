def get_book_text(path):

    with open(path) as f:
        return f.read()

def get_num_words(text):

    words = text.split()
    return len(words) 


def count_chars(text):
    character_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict


def main():

    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_chars(text)
    print(characters)

    

if __name__ == "__main__":
    main()