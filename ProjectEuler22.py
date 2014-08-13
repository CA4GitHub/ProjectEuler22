
def getNameScore(nameString):
    
    score = 0
    lowerCaseNameString = nameString.lower()
    
    for aLetter in lowerCaseNameString:
        #ord(aLetter) returns ascii value; ascii value of a is 97
        score += (ord(aLetter)-96)
    
    return score

#temporary short list of names
theNames = ["Jon", "Kate", "Bob"]
#sort is a method built into the list class
theNames.sort()
theScores = []

for aName in theNames:
    
    theScores.append(getNameScore(aName))
    #use the below print to check name and score
    #print("{0} gets a score of {1}".format(aName ,getNameScore(aName)) )