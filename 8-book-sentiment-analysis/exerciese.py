import re


def get_text():
    with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    return content


def extract_paragraphs(text, letter):
    pattern = re.compile(f"[^\n]+{letter}[^\n]+")
    findings = re.findall(pattern, text)

    return findings


if __name__ == '__main__':
    books = get_text()

    all_paragraphs = extract_paragraphs(books, 'love')
    print(all_paragraphs[:2])
