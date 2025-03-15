import sys
from stats import count_words, get_chars_dict, sort_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    char_counts = get_chars_dict(text)
    #print(char_counts)
    dictionary_list = sort_dict(char_counts)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for d in dictionary_list:
        if d["key"].isalpha() == True:
            print(f'{d["key"]}: {d["count"]}')
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()