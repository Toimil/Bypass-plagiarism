#!/usr/bin/env python3

'''
Script para conseguir pasar los programas antiplagio aun teniendo el mismo texto que otra persona, es decir, haciendo plagio.

© 2022 Toi1000, Santiago de Compostela, España ©
https://github.com/Toimil
'''

# Diccionario de caracteres a sustituir, son caracteres similares a los que se pueden introducir por teclado pero no son exactamente iguales.
dict = {'a': 'а', 'b': 'ᖯ', 'c': 'с', 'd': 'ԁ','e': 'е', 'f': 'f', 'g': 'g', 'h':'հ', 'i': 'i', 'j':'ϳ','k': '𝗄', 'l': 'l', 'm': 'm', 'n': 'ո', 'o': 'ο','p': 'р', 'q':'ԛ', 'r': 'r', 's': 's', 't': 't','u': 'ս', 'v': 'ᴠ', 'w': 'ԝ', 'x': 'х', 'y': 'у','z': 'ᴢ', 'A': 'Α', 'B': 'В', 'C': 'Ϲ', 'D': 'D','E': 'Ε', 'F': 'F', 'G': 'Ԍ', 'H': 'Η', 'I': 'I','J': 'Ϳ', 'K': 'Κ', 'L': 'Ⳑ', 'M': 'Μ', 'N': 'Ν','O': 'Ο', 'P': 'Ρ', 'Q': 'Q', 'R': 'R', 'S': 'Ѕ','T': 'Τ', 'U': 'U', 'V': 'V', 'W': 'Ԝ', 'X': 'Χ','Y': 'Υ', 'Z': 'Ζ'}

#Cambiar las palabras por caracteres similares
WORD_TRANSLATE = True
#Introducir espacios invisibles entre cada letra
BRAILLE_PATTERN_BLANK = True



def changeText(text):
    if WORD_TRANSLATE:
        for i in text:
            if i in dict:
                # Reemplazar los caracteres por los caracteres similares que se encuentran en el diccionario
                text = text.replace(i, dict[i])
    
    
    if BRAILLE_PATTERN_BLANK:
        # Introducir caracteres invisibles entre cada letra
        text = "‎".join(text)
    return text


def ask(text):
    # Preguntar si se quiere cambiar el texto o meter espacios invisibles
    while True:
        answer = input(text)
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Invalid answer, try again.")

def fileOrText():
    # Preguntar si se quiere cambiar el texto de un archivo o introducir el texto manualmente
    while True:
        answer = input("Do you want to change a file or enter text? (f/t): ")
        if answer.lower() == "f":
            # Abrir archivo
            fileName = input("Enter file name with extension: ")
            # Leer archivo si existe
            try:
                with open(fileName, "r", encoding='utf-8') as file:
                    text = file.read()
                with open("out.txt", "w", encoding='utf-8') as file:
                    file.write(changeText(str(text)))
                    print("File saved as out.txt")
            except FileNotFoundError:
                print("File not found.")
            return True
        elif answer.lower() == "t":
            text = input("Enter text: ")
            print(changeText(text))
            return False
        else:
            print("Invalid answer, try again.")


def main():
    WORD_TRANSLATE=ask("Do you want to change the words? (y/n): ")
    BRAILLE_PATTERN_BLANK=ask("Do you want to add invisible spaces? (y/n): ")
    fileOrText()
    

if __name__ == "__main__":
    main()
