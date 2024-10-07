# Count the number of words in the book
def book_to_list(book: str):
    words = book.split()
    return words


# Count word occurences
def occurrence_counter(word:str, book):
    occ = 0
    words = book_to_list(book)
    for book_word in words:
        if word.lower() == book_word.lower():
            occ += 1
    return occ

# Count letter occurences
def letter_occurence(letter, word:str):
    return word.lower().count(letter)

# Stats report
def stats(book):
    words_list = book_to_list(book)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words_list)} where found in the document")
    for alph in alphabet:
        occ = 0
        for word in words_list:
            occ += letter_occurence(alph, word)
        print(f"The {alph} character was found {occ} times")
    print("--- End report --- ")



# Main function
def main():
    with open('books/frankenstein.txt') as f:
        book = f.read()
    stats(book)



if __name__=="__main__":
    main()