import re  # importing regular expressions

""""
AUTHOR :                  Sadeed Ahmad
Program Description:      Ladder-gram program to transform a source word into a target word.
Course:                   2810ICT - Software Technologies
"""





""" This function asks the user to enter the dictionary name
and then call the load_file() function, passing the entered file name
as argument. If the file is not found, then it raises the file not 
found error"""

def file_check():
  while True:
    try:
      fname = input("Please enter the dictionary name: ")
      return load_file(fname)
    except FileNotFoundError:
      print("The file you have entered can not be found. Please try again. ")


"""This function opens the file name passed to it by the file_check 
function above"""

def load_file(file):
  return open(file, "r")


""" This function asks the user for a Start word and validates the input.
It re-prompts the user if input is invalid."""

def start_word_checker(word):as
  while True:
    if len(word) < 2:
      word = input("Start Word must be more than 2 letters. Please enter a valid start word. ")
    elif word.isalpha() == False:
      word = input("Start Word must consist of alphabets only. Please enter a valid start word. ")
    elif word.isalpha() == True:
      word.replace(" ", "")
      return word


""" This function asks the user for a Target word and validates the input.
It re-prompts the user if input is invalid."""

def target_word_checker(word):
  while True:
    if len(word) != len(start):
      word = input("Target word must be of same length as start word. Please enter a valid target word. ")
    elif word.isalpha() == False:
      word = input("Target Word must consist of alphabets only. Please enter a valid target word. ")
    elif word.isalpha():
      word.replace(" ", "")
      return word
