def get_num_words(text):

    start_marker = 'Letter 1'
    end_marker = 'End of the Project Gutenberg'
    start_index = text.find(start_marker)
    end_index = text.find(end_marker)

    if start_index != -1 and end_index != -1:
        text = text[start_index + len(start_marker):end_index].strip()
    
    text = text.replace("-\n", "")  # This joins split words across lines
    
    total_words = text.split()
    total_words = [word.strip(",.!?;:'\"-") for word in total_words]  # Remove leading/trailing punctuation
   
    return len(total_words)

def count_chars(text):
    character_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict


def get_book_report(book_path, char_dict):

    char_list = []
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for char in char_dict:
        if char.isalpha():
            char_list.append({"name": char,
                              "num": char_dict[char]})
            
    char_list.sort(reverse=True, key=sort_on)

    for char in char_list:
        print(f"{char['name']}: {char['num']}")
    
    print("============= END ===============")


def get_book_text(path):

    with open(path) as f:
        return f.read()


def sort_on(dict):
    return dict["num"]