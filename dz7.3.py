class File:
    def __init__(self, name, text):
        self.name = name
        # self.text = [line.rstrip() for line in text]
        self.text = text
        self.length = len(text)


def print_file(file):
    with open('DZ7.3.txt', 'a', encoding='utf-8') as record:
        for item in file:
            record.write(item.name)
            record.write('\n')
            record.write(str(item.length))
            record.write('\n')
            for i in range(item.length):
                record.write(item.text[i])
            record.write('\n')



with open('1.txt', 'r', encoding='utf-8') as f:
    f_lines = [l for l in f.readlines()]

with open('2.txt', 'r', encoding='utf-8') as f1:
    f1_lines = [l for l in f1.readlines()]

with open('3.txt', 'r', encoding='utf-8') as f2:
    f2_lines = [l for l in f2.readlines()]


text = File('1.txt', f_lines)
text1 = File('2.txt', f1_lines)
text2 = File('3.txt', f2_lines)

if text.length > text1.length > text2.length:
    file_list = [text, text1, text2]

if text1.length > text2.length > text.length:
    file_list = [text1, text2, text1]

if text2.length > text1.length > text.length:
    file_list = [text2, text1, text]

if text.length > text2.length > text1.length:
    file_list = [text, text2, text1]

if text1.length > text.length > text2.length:
    file_list = [text1, text, text2]

if text2.length > text.length > text1.length:
    file_list = [text2, text, text1]

print(print_file(file_list))

