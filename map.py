#! python3
# map.py -Launch a google map in the browser using address from the clipboard or command line
"""webbrowser module"""
import webbrowser
"""system module"""
import sys 
"""pyperclip module"""
import pyperclip
if len(sys.argv)> 1:
    #address from command line
    Address = ''.join(sys.argv[1:])
else:
    #address from clipboard
    Address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + Address)

