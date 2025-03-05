"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and
digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−,
letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital
letters are used. When the message is written in Morse code, a single space is used to separate the character
codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is
···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of
those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···.
These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"

"""


def decode_morse(morse_code: str):
    CODE_reversed = {'..-.': 'F', '-..-': 'X',
                     '.--.': 'P', '-': 'T', '..---': '2',
                     '....-': '4', '-----': '0', '--...': '7',
                     '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                     '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                     '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                     '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                     '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                     '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1', '   ': ' ', ' ': '',
                     '...-..-': '$'}
    # lst_morse = ' '.join([CODE_reversed[i] for i in morse_code.split(' ')])
    spaces_split = morse_code.strip().split('   ')
    sentence = []

    for word in spaces_split:
        decoded_word = ''.join(CODE_reversed[letter] for letter in word.split() if letter in CODE_reversed)
        sentence.append(decoded_word.upper())

    return ' '.join(sentence)


if __name__ == "__main__":
    print(decode_morse('.... . -.--   .--- ..- -.. .'))
