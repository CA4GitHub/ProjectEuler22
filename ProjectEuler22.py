'''This program solves the problem at https://projecteuler.net/problem=22.
   (The names.txt file can be downloaded from the above url.)
   The program reads in a file names.txt containing names enclosed in quotes and separated by commas.
   e.g. "Jon","Jenny","Bob"  
   It parses the file to produce a list of names.
   It scores the file as follows:
       1) Get the sum for each name. Each letter in a name adds a numeric value where A or a = 1 , B or b = 2, etc.
       2) Multiply the sum of step 1 by the rank of the name in the sorted list
       e.g If the first name is "Al", it's worth 1*(1 + 12) = 12.
           If the second name is "Al", it's worth 2*(1 + 12) = 24.
       3) Add the result of step 2 for all names in the list.
   Finally, the program prints the score given to the file  
'''


def getNameScore(nameString):
    
    score = 0
    lowerCaseNameString = nameString.lower()
    
    for aLetter in lowerCaseNameString:
        #ord(aLetter) returns ascii value; ascii value of a is 97
        score += (ord(aLetter)-96)
    
    return score

def scoreListOfNames(theNamesList):
    #theNamesList should be a list like ["Jon", "Kate", "Bob"]
    
    #sort is a method built into the list class
    theNamesList.sort()
    theNameScores = []

    for aName in theNamesList:
    
        theNameScores.append(getNameScore(aName))
        #use the below print to check name and score
        #print("{0} gets a score of {1}".format(aName ,getNameScore(aName)) )
        
    #multiply each name score by its rank in the list; the 0 index is rank 1
    theScores = [(i+1)*theNameScores[i] for i in range(len(theNameScores))]
    
    return sum(theScores)

def parseNamesFile(filePath):
    #filePath is a sting that is the path to a file e.g. names.txt
    
    #open the file
    nameFile = open('names.txt', encoding = 'utf-8')
    #read file; theNames contains 1 long string e.g. ["Jon","Jenney",..."Max"]
    theNamesFileString = nameFile.read()
    #parse theNames string; theNamesList contains a list e.g. ['','Jon','','Jenny',...'Max']
    theNamesList = theNamesFileString.split('"')
    #keep just the names (i.e. odd indices)
    theNamesList = [theNamesList[i] for i in range(len(theNamesList)) if i%2 != 0]
    
    return theNamesList

#main part of code
filePath = 'names.txt'
theNamesList = parseNamesFile(filePath)
score = scoreListOfNames(theNamesList)
print('The score of the file is {}.'.format(score))
