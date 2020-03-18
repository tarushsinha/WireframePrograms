import time

## run this program from the directory/folder which has the textfile in it
## when prompted to enter a filename, please be mindful of case, and specify the whole filename

options = ["1. Choose new file", "2. Print file", "3. Count letter frequency of document", "4. Exit"]

def main():
    print("Welcome to txtreader!\n")
    time.sleep(1)

    text = processFile()


    while True:
        print("\n{0}".format(options))
        response = input("\nWhat would you like to do? Please enter the corresponding option number:")

        if response == "1":
            text = processFile()

        elif response == "2":
            dump(text)

        elif response == "3":
            alphabet_freq(text)

        elif response == "4":
            exit(0)

def processFile():
    processed = False

    print(
        "When prompted to enter a filename, please be mindful of case, and specify the entire filepath: example.txt")
    time.sleep(1)

    while processed != True:
        try:
            fileName = input("\nPlease enter the name of the file which you wish to analyze:")
            with open(fileName) as file:
                text = file.read()
            processed = True
        except FileNotFoundError:
            print("\nInvalid File Name!!")

    return text

def dump(text):
    print("\n")
    print(text)

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

def alphabet_freq(text):
    print("\n")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        freq = count_char(text, letter) / len(text)
        percent = freq * 100
        print("The frequency of {0} is {1}%".format(letter, round(percent,2)))

if __name__=="__main__":
    main()
