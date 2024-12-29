def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    report = get_report(book_path, num_words, num_characters)
    return report

def get_num_characters(text):
    lowered_text = text.lower()
    overview = {}
    for character in lowered_text:
        if character in overview:
            overview[character] += 1
        else:
            overview[character] = 1
    return overview

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_report(book_path, num_words, num_characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

main()