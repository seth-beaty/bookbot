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