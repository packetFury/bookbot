import sys
from stats import word_count, character_count, character_count_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(args):
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    characters = character_count(text)
    characters_list = character_count_sorted(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in characters_list:
        for k, v in i.items():
            if k.isalpha():
                print(f"{k}: {v}")

main(sys.argv)