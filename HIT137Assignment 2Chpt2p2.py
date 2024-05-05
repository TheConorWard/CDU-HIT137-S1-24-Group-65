#Part 2 Chapter 2- Question 2

def decrypt_caesar(cryptogram, shift):
    decrypted_message = ''
    for char in cryptogram:
        if char.isalpha():
            # Determine whether to shift up or down based on uppercase or lowercase
            if char.isupper():
                decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def find_shift_key(cryptogram, original_quote):
    for shift in range(26):
        decrypted_message = decrypt_caesar(cryptogram, shift)
        if decrypted_message.lower() == original_quote.lower():
            return shift
    return None

# Original quote and cryptogram
original_quote = "Many newspapers publish a cryptogram each day for instance"
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the shift key
shift_key = find_shift_key(cryptogram, original_quote)

if shift_key is not None:
    print("Shift key:", shift_key)
    decrypted_message = decrypt_caesar(cryptogram, shift_key)
    print("Decrypted message:", decrypted_message)
else:
    print("Shift key not found.")
