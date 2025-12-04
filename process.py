# TODO: Write tests for this
def isKanji(ch) -> bool :
    ordinal = ord(ch)
    # TODO: Refactor as Match statement
    if ordinal < 0x3220 :
        return False
    if ordinal > 0x321F and ordinal < 0x3248 :
        return True
    if ordinal > 0x3247 and ordinal < 0x3280 :
        return False
    if ordinal > 0x3280 and ordinal < 0x32B1 :
        return True
    if ordinal > 0x32B0 and ordinal < 0x32C0 :
        return False
    if ordinal > 0x32BF and ordinal < 0x32CC :
        return True
    if ordinal == 0x32FF :
        return True
    if ordinal > 0x3357 and ordinal < 0x3371 :
        return True
    return ordinal > 0x337A

# TODO: Write tests for this
# The idea here is that this will take a character like U+337F, and decompose it 
# to U+682A, U+5F0F, U+4F1A and U+793E.
# To keep the scope manageable, I don't intend for this function to be used for 
# characters in the CJK Unified Ideographs block or any of the lettered 
# extension blocks.
def decompose(ch) -> str :
    return "SORRY, NOT IMPLEMENTED YET"

# TODO: Write tests for this
def pickOutKanji(s: str) -> str :
    return "SORRY, NOT IMPLEMENTED YET"
