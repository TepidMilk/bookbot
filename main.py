def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    num_words = word_count(text)
    

def get_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

main()