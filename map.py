#! python3
# map.py -Launch a google map in the browser using address from the clipboard or command line
"""webbrowser,pyperclip and system module"""
import webbrowser, sys, pyperclip
if len(sys.argv)> 1:
    #address from command line
    address = ''.join(sys.argv[1:])
else:
    #address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

