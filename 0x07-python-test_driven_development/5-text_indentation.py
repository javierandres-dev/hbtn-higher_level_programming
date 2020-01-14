#!/usr/bin/python3
def text_indentation(text):
    """ Function that prints a text with 2 new lines \
    after each of these characters: ., ? and : """
    if type(text) == str:
        text = text.replace('. ', '.\n\n')
        text = text.replace('? ', '?\n\n')
        text = text.replace(': ', ':\n\n')
        print(text)
    else:
        raise TypeError('text must be a string')
