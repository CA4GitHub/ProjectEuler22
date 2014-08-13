
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
    print(theNameScores)
    print(theScores)
    return sum(theScores)
    
#temporary short list of names
theNamesList = ["Jon", "Kate", "Bob"]
print(scoreListOfNames(theNamesList))