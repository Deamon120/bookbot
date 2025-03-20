def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("/home/damian/Project/github.com/Deamon120/bookbot/bookbot/books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
