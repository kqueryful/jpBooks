from unittest import TestCase
from format import *

class Tests(TestCase):
    def test_aozora_to_ruby_default(self):
        # test default expected behavior in converting aozora bunko formatted text to ruby tags
        test_line = r"　一行がその丘の頂《いただ》きにある尾根《おね》につきさえすれば"
        expected = "　一行がその丘の<ruby>頂<rt>いただ</rt></ruby>きにある<ruby>尾根<rt>おね</rt></ruby>につきさえすれば"
        self.assertEqual(expected, aozora_to_ruby(test_line))

    def test_punctuation(self):
        # want enclosed punctuation to be outside of the ruby tags
        test_line = "いった瞬間、《しゅんかん》"
        self.assertEqual("いった<ruby>瞬間<rt>しゅんかん</rt></ruby>、", aozora_to_ruby(test_line))

    def test_punc_double_kanji_words(self):
        test_line = "から、突然、《とつぜん》恐《おそ》ろしい"
        self.assertEqual("から、<ruby>突然<rt>とつぜん</rt></ruby>、<ruby>恐<rt>おそ</rt></ruby>ろしい", aozora_to_ruby(test_line))

    def test_em(self):
        test_line = "｜はづな《ヽヽヽ》"
        expected = "｜<b>はづな</b>"
        self.assertEqual(expected, aozora_to_ruby(test_line))

    def test_em2(self):
        test_line = "おたがいが｜またいとこ《ヽヽヽヽヽ》"
        expected = "おたがいが｜<b>またいとこ</b>"
        self.assertEqual(expected, aozora_to_ruby(test_line))