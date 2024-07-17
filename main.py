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
    

def main():
    path = "books/frankenstein.txt"
    read_file = get_file(path)
    word_count = count_words(read_file)
    print(word_count)
    character_dict = character_count(read_file)
    print(character_dict)
        

main()