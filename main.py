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


def sort_on(dict):
    return dict["num"]


def get_book_report(book_path, char_dict):

    char_list = []
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char in char_dict:
        if char.isalpha():
            char_list.append({"name": char,
                              "num": char_dict[char]})
            
    char_list.sort(reverse=True, key=sort_on)

    for char in char_list:
        print(f"The {char['name']} character was found {char['num']} times")
    
    print("--- End report ---")


def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_chars(text)
    get_book_report(book_path, characters)

    

if __name__ == "__main__":
    main()