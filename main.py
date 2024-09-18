def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    num_words = word_count(text)
    characters = char_count(text)
    book_report(get_file_name(path_to_file), num_words, characters)

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

def get_file_name(file_path):
    file = file_path.split("/")
    return file[1].strip(".txt")

def book_report(book, words, chars):
    chars_sort = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))
    print(f"--- begin report of book: {book} ---")
    print(f"{words} words found in the document \n")
    for char in chars_sort:
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")
    print("--- End Report ---")

main()