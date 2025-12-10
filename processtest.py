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
        
    def test_bopomofo_extended_are_not_kanji(self) :
        code = random.randint(0x31A0, 0x31BF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_katakana_phonetic_extensions_are_not_kanji(self) :
        code = random.randint(0x31F0, 0x31FF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_parenthesized_Korean_not_kanji(self) :
        code = random.randint(0x3200, 0x321E)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_parenthesized_kanji_are_kanji(self) :
        code = random.randint(0x3220, 0x3243)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
        
    def test_circled_ARIB_STD_B24_kanji_are_kanji(self) :
        code = random.randint(0x3244, 0x3247)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
        
    def test_circled_numbers_on_black_squares_are_not_kanji(self) :
        code = random.randint(0x3248, 0x324F)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_partnership_sign_is_not_kanji(self) :
        char = chr(0x3250)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_numbers_are_not_kanji(self) :
        code = random.randint(0x3251, 0x325F)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_hangul_letters_are_not_kanji(self) :
        code = random.randint(0x3260, 0x326D)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_hangul_syllables_are_not_kanji(self) :
        code = random.randint(0x326E, 0x327B)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_chamko_is_not_kanji(self) :
        char = chr(0x327C)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_jueui_is_not_kanji(self) :
        char = chr(0x327D)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_ieung_u_is_not_kanji(self) :
        char = chr(0x327E)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_Korean_standard_symbol_is_not_kanji(self) :
        char = chr(0x327F)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_kanji_are_kanji(self) :
        code = random.randint(0x3280, 0x32B0)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
        
    def test_more_circled_numbers_are_not_kanji_either(self) :
        code = random.randint(0x32B1, 0x32BF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
    
    def test_telegraph_month_symbols_are_kanji(self) :
        code = random.randint(0x32C0, 0x32CB)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
                
    def test_Hg_is_not_kanji(self) :
        char = chr(0x32CC)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_erg_is_not_kanji(self) :
        char = chr(0x32CD)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_eV_is_not_kanji(self) :
        char = chr(0x32CE)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_limited_liability_sign_is_not_kanji(self) :
        char = chr(0x32CF)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_circled_katakana_are_not_kanji(self) :
        code = random.randint(0x32D0, 0x32FE)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_era_name_reiwa_is_kanji(self) :
        char = chr(0x32FF)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
    
    def test_katakana_words_are_not_kanji(self) :
        code = random.randint(0x3300, 0x3357)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_telegraph_hour_symbols_are_kanji(self) :
        code = random.randint(0x3358, 0x3370)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
                
    def test_latin_abbreviations_are_not_kanji(self) :
        code = random.randint(0x3371, 0x337A)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_era_name_heisei_is_kanji(self) :
        char = chr(0x337B)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
    
    def test_era_name_syouwa_is_kanji(self) :
        char = chr(0x337C)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
    
    def test_era_name_taisyou_is_kanji(self) :
        char = chr(0x337D)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
    
    def test_era_name_meizi_is_kanji(self) :
        char = chr(0x337E)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
    
    def test_japanese_corporation_symbol_is_kanji(self) :
        char = chr(0x337F)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
    
    def test_square_latin_abbreviations_are_not_kanji(self) :
        code = random.randint(0x3380, 0x3394)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_liter_abbreviations_are_not_kanji(self) :
        for code in range(0x3395, 0x3399) :
            char = chr(code)
            message = f"Character '{char}' should not be kanji"
            assert not process.isKanji(char), message

    def test_more_square_latin_abbreviations_are_not_kanji_either(self) :
        code = random.randint(0x3399, 0x33DF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_telegraph_day_symbols_are_kanji(self) :
        code = random.randint(0x33E0, 0x33FE)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
                
    def test_gallon_abbreviation_is_not_kanji(self) :
        char = chr(0x33FF)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
    
    def test_cjk_unified_ideographs_ext_A_are_kanji(self) :
        code = random.randint(0x3400, 0x4DBF)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
                
    def test_yijing_hexagrams_are_not_kanji(self) :
        code = random.randint(0x4DC0, 0x4DFF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_cjk_unified_ideographs_are_kanji(self) :
        code = random.randint(0x4E00, 0x9FFF)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
                
    def test_other_mid_BMP_chars_are_not_kanji(self) :
        code = random.randint(0xA000, 0xABFF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message

    def test_hangul_syllables_are_not_kanji(self) :
        code = random.randint(0xAC00, 0xD7B0)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    # Deciding to skip over surrogates and private use area
        
    def test_cjk_compatibility_ideographs_are_kanji(self) :
        code = random.randint(0xF900, 0xFAD9)
        char = chr(code)
        message = f"Character '{char}' should be kanji"
        assert process.isKanji(char), message
                
    def test_alphabetic_presentation_forms_are_not_kanji(self) :
        code = random.randint(0xFB00, 0xFB4F)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    def test_arabic_presentation_forms_pre_nonchars_are_not_kanji(self) :
        code = random.randint(0xFB50, 0xFDCF)
        char = chr(code)
        message = f"Character '{char}' should not be kanji"
        assert not process.isKanji(char), message
        
    # TODO: Review characters prior to U+3358 for decompose( ) tests

    def test_decompose_telegraph_hour_symbols(self) :
        base = 0x3358
        hour_char = chr(0x70B9)
        for n in range(0, 24) :
            char = chr(base + n)
            expected = str(n) + hour_char
            actual = process.decompose(char)
            self.assertEqual(expected, actual)
    
    def test_decompose_telegraph_day_symbols(self) :
        base = 0x33DF
        day_char = chr(0x65E5)
        for n in range(1, 32) :
            char = chr(base + n)
            expected = str(n) + day_char
            actual = process.decompose(char)
            self.assertEqual(expected, actual)
    
if __name__ == '__main__' :
    unittest.main()
