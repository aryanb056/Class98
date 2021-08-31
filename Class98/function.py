def countWordsFromFile():
    fileName = input("Enter File Name")
    
    numberOfWords=0

    file = open(fileName,"r")
    for line in file:
        word=line.split()
        numberOfWords=numberOfWords+len(word)
    print("Number of Words") 
    print(numberOfWords)  

countWordsFromFile()



