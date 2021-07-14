#! python3
# map.py - Launch Google map in browser using an address from command line or clipboard.

"""webbrowser, system and pyperclip module"""
import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    # address from command line
    ADDRESS = ''.join(sys.argv[1:])
else:
    # address from clipboard
    ADDRESS = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/search/' + ADDRESS)
