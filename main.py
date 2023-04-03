# Zadanie 1
import math


def panel_calc(dl_podl, sz_podl, dl_pan, sz_pan, il_pan_w_op):
    pow_pod = (dl_podl * sz_podl) * 1.1
    pow_pan = (dl_pan * sz_pan) * 1.1
    il_pan = math.ceil(pow_pod / pow_pan)
    il_pan_w_op = math.ceil(il_pan / il_pan_w_op)

    return il_pan_w_op


print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))


# Zadanie 2
def prime(*liczby):
    lista_pierwszych = [2]
    for i in range(3, max(liczby) + 1):
        czy_pierwsza = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                czy_pierwsza = False
                break
        if czy_pierwsza:
            lista_pierwszych.append(i)

    for liczba in liczby:
        if liczba <= 1:
            print(liczba, " nie jest liczbą pierwszą")
        elif liczba in lista_pierwszych:
            print(liczba, " jest liczbą pierwszą")
        else:
            print(liczba, " nie jest liczbą pierwszą")


prime(2, 3, 4, 5, 6, 7, 8, 9, 10)


# Zadanie 3

def caesar_cipher(message, key, alphabet="abcdefghijklmnopqrstuvwxyz"):
    message = message.lower()

    encrypted_message = ""

    for letter in message:

        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = (index + key) % len(alphabet)
            encrypted_letter = alphabet[shifted_index]

            encrypted_message += encrypted_letter

        else:
            encrypted_message += letter

    return encrypted_message


enc = caesar_cipher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 5)
