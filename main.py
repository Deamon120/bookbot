import sys
from stats import count_words
from stats import sign_count
from stats import return_count_word_and_sign

#def get_book_text(path_to_file):
    #with open(path_to_file, "r", encoding="utf-8") as f:
        #return f.read()


def main():
    #book_text = get_book_text("/home/damian/Project/github.com/Deamon120/bookbot/bookbot/books/frankenstein.txt")
    #num_words = count_words(book_text)
    #num_sign = sign_count(book_text)
    #dictionary = return_count_word_and_sign(num_sign)

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    try:
        with open(book_path, 'r', encoding='utf-8') as book_file:
            text = book_file.read()
            print(f"Analyzing book found at {book_path}...")
            num_words = count_words(text)
            num_sign = sign_count(text)
            dictionary = return_count_word_and_sign(num_sign)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dictionary:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")


if __name__ == "__main__":
    main()
