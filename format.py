import re


def aozora_to_ruby(orig_text):
    """
    Convert Aozora Bunko formatted text to ruby tagged HTML
    :param orig_text: aozora-bunko formatted text
    :return: ruby tagged HTML
    """

    text = orig_text
    # paragraphs
    text = re.sub("\n", "<p>", text)

    # emphasis formatting
    # emphasis_pattern = r""
    # text = re.sub(emphasis_pattern, "<ruby>\g<text><rt>\g<emphasis></rt></ruby>", text)

    # ruby
    aozora_ruby_pattern = r"(?P<kanji>[㐀-䶵一-鿋豈-頻]+)(?P<punc>[、-〿]*)《(?P<kana>[^《]+)》"
    return re.sub(aozora_ruby_pattern, '<ruby>\g<kanji><rt>\g<kana></rt></ruby>\g<punc>', text)

if __name__ == "__main__":
    pass
    # read_file = open("boy.txt", "r")
    # write_file = open("boy_write.html", 'w')

    # write_file.write('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" class="vrtl">')
    # write_file.write('<head><meta charset="UTF-8"/></head>')

    # write_file.write(aozora_to_ruby(read_file.read()))
