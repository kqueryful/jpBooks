
import re



def aozora_to_ruby(orig_text):
    # paragraphs
    orig_text = re.sub("\n", "<p>", orig_text)

    # ruby
    aozora_ruby_pattern = r"(?P<kanji>[㐀-䶵一-鿋豈-頻]+[、]*)《(?P<kana>[^《]+)》"
    return re.sub(aozora_ruby_pattern, '<ruby>\g<kanji><rt>\g<kana></rt></ruby>', orig_text)

if __name__ == "__main__":


    test_line = "　一行がその丘の頂《いただ》きにある尾根《おね》につきさえすれば"
    print(test_line)
    print(aozora_to_ruby(test_line))

    read_file = open("boy.txt", "r")
    write_file = open("boy_write.html", 'w')

    write_file.write('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" class="vrtl">')
    write_file.write('<head><meta charset="UTF-8"/></head>')

    write_file.write(aozora_to_ruby(read_file.read()))
