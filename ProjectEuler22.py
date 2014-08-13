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
theTemp = parseNamesFile(filePath)
print(theTemp)
