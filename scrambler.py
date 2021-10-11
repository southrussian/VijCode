from itertools import cycle

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keywrd = str(input())
word = str(input())

while True:
    if keywrd == "":
        print("Keyword must not be empty!")
    elif word == "":
        print("The text must not be empty!")
    break


def encode_vijn(text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0]) +
                              alphabet.index(arg[1]) % 26) % 26]
    return ''.join(map(f, zip(text, cycle(key))))


encrypt = encode_vijn(word.upper(), keywrd.upper())
print(encrypt)


def decode_vijn(coded_text, key):
    f = lambda arg: alphabet[alphabet.index(arg[0]) - alphabet.index(arg[1]) % 26]
    return ''.join(map(f, zip(coded_text, cycle(key))))


decrypt = decode_vijn(encrypt, keywrd.upper())
print(decrypt)
