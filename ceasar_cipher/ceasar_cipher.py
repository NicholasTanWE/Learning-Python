def encrypt(text,rotation_amount):
    result = ""
    for i in range(len(text)):
        char = ord(text[i])
        if char in range(65,91):
            if char+rotation_amount<65:
                newchar = chr(char+26+rotation_amount)
            elif char <=(90-rotation_amount):
                newchar = chr(char+rotation_amount)
            else:
                newchar = chr(char-26+rotation_amount)
        elif char in range (97,123):
            if char+rotation_amount<97:
                newchar = chr(char+26+rotation_amount)
            elif char <=(122-rotation_amount):
                newchar = chr(char+rotation_amount)
            else:
                newchar = chr(char-26+rotation_amount)
        else:
            newchar=chr(char)
        result = result+newchar 
    return result
    

def count_letter_frequencies(text):
    text=text.upper()
    alphabet=[chr(65+x) for x in range(26)] # quick way to build a list of all letters in the alphabet, using a list comprehension; resulting in alphabet=['A','B',...,'Z']
    letter_frequencies={}
    for letter in alphabet:
        letter_frequencies[letter]=text.count(letter)
    return letter_frequencies

def calc_max_frequency_letter(letter_frequencies):
    most_common_letter_freq=0
    most_common_letter=""
    for key in letter_frequencies:
        if letter_frequencies[key]>most_common_letter_freq:
            most_common_letter_freq=letter_frequencies[key]
            most_common_letter=key
        else:
            continue
    return most_common_letter

    
def calculate_caesar_rotation_amount(most_common_letter):
#find ord common letter; ord("E")=69
    ord_commonletter=ord(most_common_letter.upper())
    ord_target=ord("E")
    rotation=0
    if ord_commonletter>ord_target:
        rotation=int(ord_commonletter)-int(ord_target)
    else:
        rotation=26-(int(ord_target)-int(ord_commonletter))
    return rotation
    
def break_caesar_code(coded_text):
    frequencies=count_letter_frequencies(coded_text)
    most_common=calc_max_frequency_letter(frequencies)
    rotation=calculate_caesar_rotation_amount(most_common)
    decrypted=encrypt(coded_text,rotation*-1)
    return decrypted

coded_text=input("Enter the coded text: ")
print(break_caesar_code(coded_text))
