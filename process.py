# TODO: Write tests for this
def isKanji(ch) -> bool :
    ordinal = ord(ch)
    # TODO: Refactor as Match statement
    if ordinal < 0x3220 :
        return False
    if ordinal > 0x321F and ordinal < 0x3248 :
        return True
    return ordinal > 0x327F

# TODO: Write tests for this
def pickOutKanji(s: str) -> str :
    return "SORRY, NOT IMPLEMENTED YET"
