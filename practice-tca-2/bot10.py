def under(msg):
    """
    This function creates a message and underneath converts it to *
    input: msg-string
    output: metin-string
    """
    metin = ""
    metin = metin + msg
    metin = metin + "\n"
    metin = metin + len(msg)*"*"
    return metin

def over(msg):
    metin2 = ""
    metin2 = metin2 + len(msg)*"*"
    metin2 = metin2 + "\n"
    metin2 = metin2 + msg
    return metin2

def both(msg):
    metin =""
    metin = metin + len(msg)*"*"
    metin = metin + "\n"
    metin = metin + msg
    metin = metin + len(msg)*"*"
    return metin

def grid(msg,size):
    metin = ""
    for number in range(0,size):

        metin = metin + (len(msg)*"*"+"   ")*size
        metin = metin + "\n"
        metin = metin +msg+(size-1)*(" | "+msg)
        metin = metin + "\n"
    metin = metin +(len(msg)*"*"+"   ")*size
    return metin