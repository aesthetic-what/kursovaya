def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Пример
text = "Привет, мир!"
encrypted = caesar_encrypt(text, 3)
decrypted = caesar_decrypt(encrypted, 3)

print("Исходный текст:", text)
print("Зашифрованный:", encrypted)
print("Расшифрованный:", decrypted)







def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

