#! python3
''' Script works same as built-in strip() function. It removes
whitespace characters or chars provided through optional argument
from beginning and end of the given string.'''
import re

def customStrip(string, toRemove='\s'):
    wordbeginRegex = re.compile(r'^['+ toRemove+']+')
    string = wordbeginRegex.sub('', string)
    wordendRegex = re.compile(r'['+ toRemove+']+$')
    string = wordendRegex.sub('', string)
    return string
