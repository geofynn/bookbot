def get_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file):
    file_as_string = file.split()
    counter = 0
    for word in file_as_string:
        counter += 1
    return counter

def character_count(file):
    character_dict = {}
    file = file.lower()
    file_as_array = file.split()
    #print(file_as_array)
    for word in file_as_array:
        for character in word:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def print_Report(word_count, character_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    character_list = character_dict.items()
    dict_array = []
    for item in character_list:
        if item[0].isalpha() == True:
            dict_array.append({"character": f"{item[0]}", "num": item[1]})
    dict_array.sort(reverse=True, key=sort_on)
    for item in dict_array:
        print("The ", item["character"], " character was found ", item["num"],  " times")
    print("--- End report ---")



def main():
    path = "books/frankenstein.txt"
    read_file = get_file(path)
    word_count = count_words(read_file)
    character_dict = character_count(read_file)
    print_Report(word_count, character_dict)
        

main()