def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_list = get_list_of_words_in_book(book_text)
    word_count = dict_count_all_characters(word_list)
    print_word_count_report(word_count)
    
    
def print_word_count_report(dict_of_word_count: dict[str, int]) -> None:
    for word in dict_of_word_count:
        print(f"The '{word}' character was found '{dict_of_word_count[word]}' times")
    
    print("\n----------- End report -----------")



def get_book_text(path: str) -> str:
    with open(path) as f:
        text = f.read()
        return text
    
def get_list_of_words_in_book(text) -> list:
    return text.split()


def get_word_count_in_book(text) -> int:
    return len(get_list_of_words_in_book(get_book_text))

def dict_count_all_characters(list_of_words: list[str]) -> dict:
    character_count_dict = {}
    for word in list_of_words:
        for character in word:
            lower_case_char = character.lower()
            if lower_case_char not in character_count_dict:
                character_count_dict[lower_case_char] = 1
            else:
                character_count_dict[lower_case_char] += 1

    return character_count_dict



main()