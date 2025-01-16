def format_output(word_count, char_dict):
    result = '--- Begin report of books/frankenstein.txt ---\n'
    result += '{} words found in the document\n\n'.format(word_count)
    for key, value in char_dict.items():
        if key == '\n':
            key = '\\n'
        result += 'The {} character was found {} times\n'.format(key, value)
    result += '--- End report ---'
    return result


def char_count(s):
    char_dict = {}
    for char in s:
        char = char.lower()
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def word_count(s):
    return len(s.split())


def main():
    file_contents = ''
    with open('./books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    print(format_output(word_count(file_contents), char_count(file_contents)))


if __name__ == '__main__':
    main()
