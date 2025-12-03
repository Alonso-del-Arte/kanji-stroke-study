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
    return ordinal > 0x337A and ordinal < 0x337F

# TODO: Write tests for this
def pickOutKanji(s: str) -> str :
    return "SORRY, NOT IMPLEMENTED YET"
