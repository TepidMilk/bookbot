def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)

def get_text(path):
    with open(path) as f:
        return f.read()
    
main()