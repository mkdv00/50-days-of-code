import re


def read_text(filename='miracle_in_the_andes.txt', encoding='utf-8'):
    """Read the file and return content as a string"""
    with open(filename, 'r', encoding=encoding) as file:
        book = file.read()

    return book


def count_of_items(items_list, find_str):
    """Return the count of all items"""
    return f"Count {find_str}: {len(items_list)}"


def common_find_all(pattern, text):
    # Make a pattern for searching
    pattern = re.compile(pattern)
    # Find all strings in text by pattern
    all_str = re.findall(pattern, text)

    return all_str


def find_all_chapters(text):
    """Find for all 'Chapter'"""
    chapters = common_find_all('Chapter [0-9]', text)
    return chapters


def find_all_love(text):
    """Find for all 'love'"""
    loves = common_find_all('[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.', text)
    return loves


def find_all_str(text):
    all_str = common_find_all('[a-zA-Z]+', text.lower())
    return all_str


def count_all_letters(words):
    d = {}

    for word in words:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1

    d_list = [(value, key) for (key, value) in d.items()]
    d_list_sorted = sorted(d_list, reverse=True)

    return d_list_sorted


def main():
    books = read_text()
    chapters = find_all_chapters(books)
    loves = find_all_love(books)

    print(count_of_items(chapters, 'Chapters'))
    print(chapters)

    print(count_of_items(loves, 'loves'))
    print(loves)

    all_text = find_all_str(books)
    print(count_all_letters(all_text))


if __name__ == '__main__':
    main()
