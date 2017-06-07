import re

def em_format(text):
    """
    helper function
    :param text: emphasized expression
    :return: emphasized expression in HTML tags
    """
    em = text.count('ヽ')

    # not emphasized = length of emphasis *2 + 2 parentheses
    front = len(text) -em*2 -2

    # return with tags, without parentheses
    # return text[:front] + "<ruby>" + text[front:front+em] + "<rt>" + text[front+em+1:-1] + "</rt></ruby>"
    return text[:front] + "<b>" + text[front:front+em] + "</b>"


def aozora_to_ruby(orig_text):
    """
    Convert Aozora Bunko formatted text to ruby tagged HTML
    :param orig_text: aozora-bunko formatted text
    :return: ruby tagged HTML
    """
    kanji = r'㐀-䶵一-鿋豈-頻'
    symbols_punct = r'、-〿'

    text = orig_text

    # paragraphs
    text = re.sub("\n", "<p>", text)

    # emphasis formatting
    emphasis_pattern = r"[^》]+《[ヽ]+》"
    text = re.sub(emphasis_pattern, lambda x: em_format(x.group()) , text)

    # ruby
    aozora_ruby_pattern = r"(?P<kanji>[" + kanji + "]+)(?P<punc>["+ symbols_punct +"]*)《(?P<kana>[^《]+)》"
    return re.sub(aozora_ruby_pattern, '<ruby>\g<kanji><rt>\g<kana></rt></ruby>\g<punc>', text)

if __name__ == "__main__":


    # pass
    read_file = open("boy.txt", "r", encoding="shiftjis").read()
    write_file = open("boy_write.html", 'w')

    write_file.write('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" class="vrtl">')
    # write_file.write('<head><meta charset="UTF-8"/></head>')

    write_file.write(aozora_to_ruby(read_file))
