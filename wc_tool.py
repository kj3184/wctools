import os
import re
import sys


def countlines(filename):
    try:
        with open(filename, "r") as textfile:
            lines = textfile.readlines()
            return len(lines)
    except FileNotFoundError:
        print("No such file " + filename + " found")
        return False


def countbytes(filename):
    bytes_count = 0
    if os.path.isfile(filename):
        bytes_count = os.stat(filename).st_size
        return bytes_count
    else:
        print("No such file " + filename + " found")
        return False


def countchars(filename):
    try:
        character_count = 0
        with open(filename, "r") as filedata:
            text = filedata.read()
            # Remove whitespace characters
            character_count = len(re.sub(r"\s+", "", text, flags=re.UNICODE))
            return character_count
    except FileNotFoundError:
        print("No such file " + filename + " found")
        return False


def countwords(filename):
    try:
        with open(filename, "r") as textfile:
            text = textfile.read()
            words = re.findall(r"\b\w+\b", text)
            return len(words)
    except FileNotFoundError:
        print("No such file " + filename + " found")
        return False


def check_option(switchoption):
    match switchoption:
        case "-l":
            print("\nThe No. of lines in " + filename + ":" + str(countlines(filename)))
        case "-b":
            print("\nThe No. of bytes in " + filename + ":" + str(countbytes(filename)))
        case "-c":
            print(
                "\nThe No. of characters in "
                + filename
                + ":"
                + str(countchars(filename))
            )
        case "-w":
            print("\nThe No. of words in " + filename + ":" + str(countwords(filename)))


switchoption = sys.argv[1]
filename = sys.argv[2]

check_option(switchoption)
print("\n")
