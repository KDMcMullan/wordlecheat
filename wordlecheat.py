import os , sys
from random import random

# these letters must not appear
exclude=""

# these letters must be in these positions
inpos="-----"

# these letters must not be in these positions
notinpos=["-----","-----","-----"]

avoidDupLetters = False # avoid words with duplicate letters

buildRequired = True # automatically build list of implied required letters

# number of words for initial run; 0 = don't do initial run
initialCount = 0

### TO DO ###
sortByPop = True # sort by commonality of letters

# Main Program Starts Here

# check that
# 1) nothing in "exclude" is also in "inpos"
# 2) nothing in "exclude" is also in "notinpos"
# 3) nothing in "inpos" is at the same position as "notinpos"

failInputs = False
conflictEx = ""
conflictIm = ""
for letter in exclude:
  if letter in inpos:
    conflictEx += letter
    failInputs = True
  for imPos in notinpos:
    if letter in imPos:
      conflictIm += letter
      failInputs = True
if conflictEx == "":
  print("No explicit letters in the excluded list.")
else:
  print(f"*** Excluded and explicit lists both contain: {conflictEx}.")
if conflictIm == "":
  print("No implicit letters in the excluded list.")
else:
  print(f"*** Excluded and implicit lists both contain: {conflictIm}.")
conflictIm = ""
for imPos in notinpos:
  for l in range(0,len(inpos)):
    letter = imPos[l]
    if letter != "-" and letter == inpos[l]:
      conflictIm += letter
      failInputs = True
if conflictIm == "":
  print("No explicit letters in the implicit places.")
else:
  print(f"*** Explicitly placed letters in implicit places: {conflictIm}.")

if not failInputs:

  myPath = os.path.abspath(os.path.dirname(sys.argv[0])) # path to this script
  datafile = myPath + "/5letterwords.txt"

  print(datafile)

  if initialCount != 0:
    avoidDupLetters = True # avoid words with duplicate letters

  words=[]
  lineCount = 0
  rejectCount = 0
  dupeLettCount = 0

  with open(datafile,"r") as f:
    word=f.readline().upper() # read line-at-a-time, converting to ucase
    while word:
      word=word.strip()       # strip newline, etc.
      lineCount += 1          # count the lines read
      if len(word) == 5:      # only keep 5 letter words
        if word in words:
          rejectCount +=1
        else:

          dupeLett = False
          if avoidDupLetters: # check for duplicate letters
            for p1 in range(0,len(word)-1):
              for p2 in range(p1+1,len(word)):
                if word[p1]==word[p2]:
                  dupeLett = True

          if dupeLett:
            dupeLettCount +=1
          else:
            words.append(word)

      word=f.readline().upper()
  f.close()

  print(f"{lineCount} lines read, {rejectCount} duplicate entries. {dupeLettCount} rejected for duplicate letters.")
  print(f"{len(words)} words recovered.")
        
  if initialCount != 0: # show 'initialCount random words which don't contain duplicate letters

    print(f"Here are {initialCount} at random.")
    print()

    for n in range(0,initialCount):
      print(words[int(random()*len(words))])

  else:

    print()

    required = "" # calculate which letters are required
    if buildRequired:
      for nip in notinpos:
        for ch in nip:
          if ch != "-" and not ch in required:
            required += ch

    excount = 0
    reqcount = 0
    wrongposcount = 0
    notrightposcount = 0
    wordcount = 0

    tab = 0 # print column
    for word in words:

      found = False # discard words containing excluded lettters
      for letter in exclude:
        if letter in word:
          found = True

      if found:
        excount +=1

      else:
        found = True # discard words not containing all required letters
        for letter in required:
          if not letter in word:
            found = False

        if not found:
          reqcount +=1

        else:
          found = False # discard words containing letters in the wrong positions
          for notpos in notinpos:
            pos = 0
            for ch in notpos:
              if ch != "-" and ch == word[pos]:
                found = True
              pos +=1

          if found:     
            wrongposcount +=1

          else:
            found = True # discard words not containing letters in the correct positions
            pos = 0
            for inch in inpos:
              if inch != "-" and word[pos] != inch:
                found = False
              pos +=1  
            if found:
              tab += 1
              if tab >= 10:
                tab = 0
                print(word)
              else:
                print(f"{word}  ", end = "")
              wordcount +=1
            else:
              notrightposcount +=1

    if tab < 10:
      print()
    print()
    print(f"{excount} words rejected for containing excluded letters \"{exclude}\",")
    print(f"{reqcount} more rejected for not containing required letters \"{required}\",")
    print(f"of which {wrongposcount} were rejected for letters in the wrong place,")
    print(f"with another {notrightposcount} rejected for letters not in the expected place,")
    print(f"leaving {wordcount} matching words.")
