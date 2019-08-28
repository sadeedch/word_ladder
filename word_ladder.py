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



""" This function builds the list of words which the user wants to omits from the target word process. """

def excluded_words_build(words):
  excluded_words = words.split(',')
  return excluded_words


"""This function returns the number of letters of each item which
 matches the target word. """

def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])


"""This function returns a list of words that matches the pattern which is provided
as an input. It ensures that the word is not already in the seen dictionary. """

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                 word not in list]


""" This function iterates over each word and moves gradually towards the target"""

def find(word, words, seen, target, path):
  matched_letters = []
  list = []

  # same() function is being called here.
  if same(word, target) > 0:
    # after comparing the new start word and the target word, it returns a list of indexes of letters which are matched.
    matched_letters = [i for i, x in enumerate(zip(word, target)) if all(y == x[0] for y in x)]


  for i in range(len(word)):
    if i not in matched_letters: # It builds the pattern for letter positions which have not already been found
      # It builds the list of words matching the pattern where letter has not been found.
      list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  # if the list is empty, exit the iteration.
  if len(list) == 0:
    return False

  # this sorts the list alphabatically and by number of matches.
  list = sorted([(same(w, target), w) for w in list], reverse=True)
  for (match, item) in list:
    # if word matches target or 1 letter off target.
    if match >= len(target) - 1:
      if match == len(target) - 1:
        # it appends the word to the path and exit as the last word has been found.
        path.append(item)
      return True
    # This marks each word in the current list to True, so it is excluded from the future search.
    seen[item] = True
  for (match, item) in list:
    path.append(item)   # appends the item to the path.
    if find(item, words, seen, target, path):  # recursively calling itself.
      return True
    path.pop() # inbuilt pop() function is being called, to remove the last word in path if a path for the item is not found.


file = file_check()  # file_check() function defined above is being called here.
lines = file.readlines()  # readlines() function is being called on the dictionary file.


"""
This function asks the user for required inputs while also validating those inputs by 
applying the functions defined above. 
"""
while True:
  word = input("Please enter the start word:")  # asks the user for start word input
  start = (start_word_checker(word))            # Validates the start word input by applying start_word_checker function.
  word = input("Please enter the target word:") # asks the user for target word input
  target = (target_word_checker(word))          # Validates the target word input by applying target_word_checker function.

  #asks the user if they want to ignore any words during the target process or they can leave this empty.
  excluded_list = str(input("Please enter the words to ignore, separated by commas or leave this field empty\n"
                            "Here is an example of how to format your input: \ndeep, heap, beep\n")).replace(" ","")
  # builds the list of all the words to ignore  as given by user by applying excluded_words_build() function.
  excluded_words = excluded_words_build(excluded_list)

  # builds the words list by not having any excluded words in that list.
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start) and word not in excluded_words:
      words.append(word)
  break



count = 0
path = [start]
seen = {start : True}

# Calls the find() function for the first iteration.
if find(start, words, seen, target, path):
    path.append(target)   # appends the target to the path list.
    print(len(path) - 1, path) # prints the path list and the length of the path.
else:
  print("No path found")

