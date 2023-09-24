#Morse Code Translator
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += char + " "
    return morse_code.strip()


def morse_to_text(morse_code):
    text = ""
    morse_code = morse_code.split(" ")
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
                break
        else:
            text += code
    return text


def morse_code_translator():
    print("Morse Code Translator")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the text to convert to Morse Code: ")
            morse_code = text_to_morse(text)
            print("Morse Code:", morse_code)
        elif choice == '2':
            morse_code = input("Enter the Morse Code to convert to text: ")
            text = morse_to_text(morse_code)
            print("Text:", text)
        elif choice == '3':
            print("Thank you for using the Morse Code Translator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


morse_code_translator()