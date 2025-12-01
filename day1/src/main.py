import re

def GetResult(input):
    currentNumber = 50
    zeroCounter = 0
    
    for line in input:
        direction = line[0]
        number = int(re.findall(r'\d+', line)[0])
        # normalize the number:
        while number > 99:
            number -= 100

        if direction == "L":
            currentNumber -= number
        elif direction == "R":
            currentNumber += number
        
        # overflow scenarios
        if currentNumber > 99:
            currentNumber -= 100
        elif currentNumber < 0:
            currentNumber = 100 + currentNumber
            
        if currentNumber == 0:
            zeroCounter += 1
            
    return zeroCounter 

if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        result = GetResult(file)
        print(f"Answer: {result}")