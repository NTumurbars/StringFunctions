def mainProgram():
        
    strInput = str(input("Please enter your string: "))
    
    print("Number of characters in string without space: " + str(charNumberCount(strInput)))
    print("Number of vowels in string: " + str(vowelNumberCount(strInput)))
    print("Number of digits in string: " + str(digitNumberCount(strInput)))

#Except white space
def charNumberCount(strInput):

    
    spaceCount = strInput.count(" ")
    
    count = len(strInput) - spaceCount
    
    return count

def vowelNumberCount(strInput):
    
    vowels = ['a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'U', 'O']
    count = 0
    for char in strInput:
        if char in vowels:
            count = count + 1
    return count

def digitNumberCount(strInput):
    
    count = 0
    for char in strInput:
        if char.isdigit():
            count = count + 1
    return count

if __name__ == "__main__":
    mainProgram()


        
