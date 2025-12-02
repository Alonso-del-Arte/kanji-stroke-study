# TODO: Write tests for this
def isKanji(ch) -> bool :
    ordinal = ord(ch)
    # TODO: Refactor as Match statement
    if ordinal < 0x3220 :
        return False
    if ordinal > 0x321F and ordinal < 0x3248 :
        return True
    if ordinal > 0x32BF and ordinal < 0x32CC :
        return True
    return ordinal > 0x3280 and ordinal < 0x32B1

# TODO: Write tests for this
def pickOutKanji(s: str) -> str :
    return "SORRY, NOT IMPLEMENTED YET"
