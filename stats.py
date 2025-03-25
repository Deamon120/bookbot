def count_words(text):
    words = text.split()
    return len(words)


def sign_count(text):
    words = text.split()
    letter_count = {}
    for word in words:
        letters = list(word.lower())
        for letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    space_count = count_words(text)
    letter_count[" "] = space_count     
    return letter_count

def return_count_word_and_sign(char_dict):
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict
