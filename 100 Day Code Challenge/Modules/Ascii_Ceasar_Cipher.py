def encrypt (text, shift):
    shifted_text =''
    for i in range(len(text)):
        a = ord(text[i])+shift
        if a>122:
            a-=26
        shifted_text+=chr(a)
    print(shifted_text)