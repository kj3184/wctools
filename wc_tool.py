import os
import re


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
