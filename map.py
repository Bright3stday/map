#! python3
# map.py -Launch a google map in the browser using address from the clipboard or command line
"""webbrowser module"""
"""system module"""
"""pyperclip module"""
import webbrowser
import sys 
import pyperclip
if len(sys.argv)> 1:
    #address from command line
    ADDRESS = ''.join(sys.argv[1:])
else:
    #address from clipboard
    ADDRESS = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + ADDRESS)
