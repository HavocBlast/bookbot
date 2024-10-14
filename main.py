def get_book_content(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(content):
    words = content.split(" ")
    return len(words)

def get_character_count(content):
    chars_used = {}
    lowered_text = content.lower()
    for text in lowered_text:
        if text in chars_used:
            chars_used[text] += 1
        else:
            chars_used[text] = 1
    return chars_used

def generate_report(book_location):
    word_count = get_word_count(get_book_content(book_location))
    character_count = get_character_count(get_book_content(book_location))
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")
    for char in character_count:
        print(f"The '{char}' character was found {character_count[char]} times")
    print("--- End Report ---")

def main():
    book_location = "./books/frankenstein.txt"
    generate_report(book_location)
    return 0

main()
