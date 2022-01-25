
#question 1
def isVowelOrConst(str):
    vowel = 0
    const = 0
    for x in str:
        if set('aeiou').intersection(x.lower()):
            vowel = 1 + vowel
        else:
            const = 1 + const

    if vowel > const:
        return True
    if const > vowel:
        return False
    if const == vowel:
        return None

print(isVowelOrConst("Ash")) #should return False

#question 2
import math
def volume(radius, height):
    v = math.pi * height * (radius*radius)

    return v

print(volume(2, 3)) #should return 37.7

#question 3 
def commaSeparate(str):
    new_string = ",".join(str) #takes the first element and separates list via this
    return new_string


colors = ["red", "orange", "yellow"]
print(commaSeparate(colors))

#question 4
import pandas as pd
import os
def listOfLists(str):
    df = pd.DataFrame(str)
    df.to_csv('q4output.csv', index=False, header=False) #don't want row/column indexes so set to False
    return os.path.abspath('q4output.csv')

colors = [["red", "orange", "yellow"], 
         ["green", "blue", "purple"],
         ["pink", "brown", "black"]]
print(listOfLists(colors))

#question 5 
def readFile(fileName):
    df = pd.read_csv(fileName)
    return list(df)

print(readFile('q4output.csv'))

#question 6
def errorHandling(x, y):
    try:
        return x/y
    except:
        if y == 0:
            return "Cannot divide by 0"
print(errorHandling(2, 0))

#question 7
def noDup(nums):
    return list(set(nums))
nums = [1, 1, 2, 4, 6, 6, 8]
print(noDup(nums))

#question 8
import os
def newFolder(name):
    os.mkdir(os.path.join("/Users/ashwiniaphale/Documents/SWE/HW", name))
    return os.path.abspath(name)
print(newFolder("hw3-folder"))