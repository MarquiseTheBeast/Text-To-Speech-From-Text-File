from pathlib import Path
import pyttsx3 as tts

''' This program is a text-to-speech conversion using the pyttsx3 library that will read and speak each line inside the text file. '''

# Constant
TEXT_FILE = Path(__file__).resolve().parent / "text.txt"    # Text file in the same folder

def main():
    # Check to make sure file exists in same folder
    if TEXT_FILE.exists():
        writing_to_file()
        reading_file()
    else:
        print(f"Error: {TEXT_FILE.name} not found.")

# Writing text to the file
def writing_to_file():
    good_value_received = False
    while not good_value_received:
        try:
            # Entering the number of lines you want in the text file
            # If detected as non-integer, user will be prompted to enter again
            number_of_lines = int(input("How many number of lines do you want in the text file?: "))

            # Opening the text file for writing
            with open(TEXT_FILE, 'w') as file:
                # Loop for writing text on each line
                for line in range(number_of_lines):
                    # The user types any text for each line before writing to the text file.
                    text = input(f"Type any text for line {line + 1}: ")
                    file.write(text + '\n')
                good_value_received = True
                print()
        except ValueError:
            print("Invalid input. Value must be an integer. Please try again.")

# Reading each line in the text file
def reading_file():
    try:
        # Opening the same text file again for reading 
        with open(TEXT_FILE, 'r') as read_file:
            # Read each line in the text file for text-to-speech
            for line in read_file:
                print(line)
                tts.speak(line)
    except FileNotFoundError as file_error:
        print(file_error)

if __name__ == '__main__':
    main()

