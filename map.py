"""webbrowser, system and pyperclip module"""
import sys
import webbrowser

import pyperclip

if len(sys.argv)> 1:
    #address from command line
    ADDRESS = ''.join(sys.argv[1:])
else:
    #address from clipboard
    ADDRESS = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + ADDRESS)