def count_chars(book_content):
    lowered_case_content = book_content.lower()
    result = {}
    for char in lowered_case_content:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def count_words(book_content):
     return len(book_content.split())

def book_report(num_of_chars):
    report_list = []

    for i in num_of_chars:
        if i.isalpha():
            report_list.append({'char': i, "num": num_of_chars[i]})

    return report_list

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        num_of_words = count_words(file_contents)
        num_of_chars = count_chars(file_contents)
        report_list = book_report(num_of_chars)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_of_words} words found in the document\n")
        report_list.sort(reverse=True, key=sort_on)
        for line in report_list:
            print(f"The '{line["char"]}' character was found {line["num"]} times")
        print("--- End report ---")

main()