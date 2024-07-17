

def __main__():
    with open("books/frankenstein.txt") as b:
        file_contents = b.read()
        print(count_words(file_contents) + " words found in the document")
        print("\n")
        letters = sort_on(count_letters(file_contents))
        for k in letters:
            print(f'The "{k}" character was found {letters[k]} times')
        print("--- End report ---")

def count_words(contents: str):
    words = contents.split()
    return len(words)

def count_letters(contents: str):
    letters = {}
    lower_content = contents.lower()
    for i in lower_content:
        if 'a' <= i <= 'z':
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1
    return letters

def sort_on(diction):
    sorts = sorted(diction.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorts)
    return sorted_dict

__main__()
