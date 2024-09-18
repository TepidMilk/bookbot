def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    num_words = word_count(text)
    characters = char_count(text)
    

def get_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


main()