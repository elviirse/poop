
# Decoding the ASCII code sequence into text

# ASCII code list
ascii_codes = [0, 2] #, 105, 115, 105, 97, 32, 75, 105, 101, 108, 105, 228]

# Convert each ASCII code to its corresponding character and join into a string
decoded_text = ''.join(chr(code) for code in ascii_codes)
print(decoded_text)
"""
# Salakirjoitettu teksti
encrypted_message = ",soypl’ttuy pbsy tollo"

# 1. Kirjainten järjestyksen kääntö
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())

# 2. Caesar-siirto: kokeillaan eri siirtoarvoja (1–25) ja tulostetaan tulokset
def caesar_shift(text, shift):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char  # Jätetään erikoismerkit ennalleen
    return result

# Tulostetaan eri ratkaisut
print("Käänteinen:", reverse_words(encrypted_message))
print("Caesar-siirrot:")
for shift in range(1, 26):
    print(f"Siirto {shift}: {caesar_shift(encrypted_message, shift)}")
"""
import itertools
import string
from collections import Counter

# Salakirjoitettu teksti
encrypted_message = ",soypl’ttuy pbsy tollo"

# 1. Vigenère-salaus, jossa testataan useita avainsanoja
def vigenere_decrypt(text, key):
    decrypted_text = ""
    key = itertools.cycle(key)  # Toistetaan avainsanaa tekstin pituuden verran
    for char, k in zip(text, key):
        if 'a' <= char <= 'z':  # Käytetään vain aakkosia
            shift = ord(k) - ord('a')
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

# Esimerkki avainsanoista, joita voi kokeilla
keys = ["secret", "koodi", "avain", "vaarallinen"]

print("Vigenère-salauksen purku:")
for key in keys:
    print(f"Avainsana '{key}':", vigenere_decrypt(encrypted_message, key))


# 2. Kirjainten vaihtotaulu
def substitution_decrypt(text, substitution_table):
    return ''.join(substitution_table.get(char, char) for char in text)

# Esimerkki satunnaisesta vaihtotaulusta (voit kokeilla vaihtamalla kirjaimia)
substitution_table = {
    's': 'e', 'o': 't', 'y': 'a', 'p': 'h', 'l': 'i', 't': 's', 'u': 'n', 'b': 'r'
}

print("\nKirjainten vaihtotaulun purku:", substitution_decrypt(encrypted_message, substitution_table))


# 3. Anagrammien kokeilu
def generate_anagrams(word):
    return [''.join(perm) for perm in itertools.permutations(word)]

first_word, second_word, third_word = encrypted_message.split()

print("\nAnagrammi-ehdotuksia ensimmäiselle sanalle:")
anagrams_first = generate_anagrams(first_word.strip(",’"))
print(anagrams_first[:10])  # Tulostetaan vain ensimmäiset 10 mahdollista anagrammia

print("\nAnagrammi-ehdotuksia toiselle sanalle:")
anagrams_second = generate_anagrams(second_word)
print(anagrams_second[:10])
