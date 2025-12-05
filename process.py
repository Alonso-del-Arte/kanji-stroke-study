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
    if ordinal > 0x337A and ordinal < 0x3380 :
        return True
    return ordinal > 0x33DF and ordinal < 0x33FF

# TODO: Write a lot more tests for this
# The idea here is that this will take a character like U+337F, and decompose it 
# to U+682A, U+5F0F, U+4F1A and U+793E.
# To keep the scope manageable, I don't intend for this function to be used for 
# characters in the CJK Unified Ideographs block or any of the lettered 
# extension blocks.
def decompose(ch) -> str :
    ordinal = ord(ch)
    if ordinal > 0x33DF and ordinal < 0x33FD :
        num_str = str(ordinal - 0x33DF)
        return num_str + chr(0x65E5)
    num_str = str((ordinal % 0x100) - 0x58)
    return num_str + chr(0x70B9)

# TODO: Write tests for this
def pickOutKanji(s: str) -> str :
    return "SORRY, NOT IMPLEMENTED YET"
