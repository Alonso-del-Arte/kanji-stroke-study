import random
import unittest

import process

class ProcessTest(unittest.TestCase) :

    def test_ASCII_C0_control_char_is_not_kanji(self) :
        code = random.randint(0, 31)
        control_char = chr(code)
        message = f"Character for code {code} should not be kanji"
        assert not process.isKanji(control_char), message

    def test_ASCII_char_is_not_kanji(self) :
        code = random.randint(32, 126)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_ASCII_C1_control_char_is_not_kanji(self) :
        code = random.randint(0x80, 0x9F)
        control_char = chr(code)
        message = f"Character for code {code} should not be kanji"
        assert not process.isKanji(control_char), message

    def test_other_low_BMP_char_is_not_kanji(self) :
        code = random.randint(0xA0, 0x2FFF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_CJK_symbols_and_punctuation_are_not_kanji(self) :
        code = random.randint(0x3000, 0x303F)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
    
    def test_hiragana_are_not_kanji(self) :
        code = random.randint(0x3041, 0x309F)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_katakana_are_not_kanji(self) :
        code = random.randint(0x30A0, 0x30FF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_bopomofo_are_not_kanji(self) :
        code = random.randint(0x3105, 0x312F)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_compat_hangul_are_not_kanji(self) :
        code = random.randint(0x3131, 0x318E)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
    
    # TODO: Determine if kanbun should be treated as kanji or not
        
if __name__ == '__main__' :
    unittest.main()
