def caesar(text, shift, encrypt = True):
    if not isinstance(shift, int):
        return 'Shift must be a whole number'
    if shift < 1 or shift > 25:
        return 'Shift must be between 1 and 25'
    
    

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if not encrypt:
          shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
        return caesar(text, shift)
        
def decrypt(text, shift):
        return caesar(text, shift, encrypt = False)

encrypt_this = 'Hello, world!'

print(encrypt(encrypt_this, 5))

