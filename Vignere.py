"""
Vignere Cipher
Practice project as part of a symmetric cryptography course on Coursera.
This program will prompt the user to enter a plain-text message and an encryption key through
the command line. Using a Vignere Cipher, it will print the plain-text message and the cipher-text
generated using the encryption key, then print the decrypted plain-text once again.
"""

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')  # creates alphabet as a list to reference in algorithm


# takes input of text on command line if accepts parameters
def get_input(prompt):
    while True:  # loop until successful input
        input_text = input(prompt).casefold().replace(" ", "")
        if input_text.isalpha():
            return list(input_text)  # at this point, should be all lowercase alphabets no spaces
        else:
            print("Try again.")  # prompts reattempt if entry is not usable in my algorithm (if not above conditions)


# uses key and a starting text to create a new text
def convert(key, oldtext, direction):  # takes boolean parameter to signify encryption or decryption
    text = []
    for i in oldtext:  # loop finds an int value for each character in text and corresponding key position
        k_value = key.pop(0)
        new_char = encrypt_decrypt(ALPHABET.index(i), ALPHABET.index(k_value), direction)  # finds int of new character
        text.append(ALPHABET[new_char])  # after finding new int adds corresponding character to new text
        key.append(k_value)  # to continue cycling through key
    return text


# uses int values representing starting point and shift, for encryption and decryption
def encrypt_decrypt(int1, int2, encrypt):
    if encrypt:  # if received true, encrypt value returning int mod 26
        return (int1 + int2) % 26
    else:  # otherwise, decrypt value
        return (int1 - int2) % 26


def main():
    pt = get_input("Please enter a message (using no special characters or punctuation): ")
    print("Message is " + ''.join(pt))
    print()
    k = get_input("Please enter a word or phrase to be used as an encryption key (letters only): ")
    print()
    ct = convert(k.copy(), pt, True)  # TRUE will encrypt message; copies key as order will be changed
    print("Your encrypted message is: " + ''.join(ct))
    print()
    ft = convert(k.copy(), ct, False)  # FALSE will decrypt; again copies key
    print("Your message was: " + "".join(ft))
    print()


if __name__ == '__main__':
    main()
