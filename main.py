def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    list_characters = get_list_characters(num_characters)
    report = get_report(book_path, num_words, list_characters)
    return report


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    lowered_text = text.lower()
    overview = {}
    for character in lowered_text:
        if character in overview:
            overview[character] += 1
        else:
            overview[character] = 1
    return(overview)
    
    
def get_list_characters(num_characters):
    list_of_dicts = [{"key": key, "count": count} for key, count in num_characters.items()]
    sorted_list = sorted(list_of_dicts, key=lambda x: x['count'], reverse=True)
    letters_only = [entry for entry in sorted_list if entry['key'].isalpha()]
    return letters_only

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_report(book_path, num_words, list_characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for entry in list_characters:
        print(f"The '{entry['key']}' character was found {entry['count']} times")
    print("--- End report ---")

main()