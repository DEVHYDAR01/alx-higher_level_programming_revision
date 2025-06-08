#!/usr/bin/env python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        if char in [".", "?", ":"]:
            result = result + char + "  "
        else:
            result += char
    sep_chars = result.split("  ")
    cleaned = [part.strip() for part in sep_chars if part.strip()]
    for i in range(len(cleaned)):
        print(cleaned[i])  # Print the sentence
        if i != len(cleaned) - 1:
            print()




