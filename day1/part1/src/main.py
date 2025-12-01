import re

def NormalizeNumber(number):
    while number > 99:
        number -= 100

    if number < 0:
        number = 100 + number
 
    return number

def GetResult(input):
    dial = 50
    zeroCounter = 0
    
    for line in input:
        direction = line[0]
        numberToRotate = int(re.findall(r'\d+', line)[0])
        numberToRotate = NormalizeNumber(numberToRotate)

        if direction == "L":
            dial -= numberToRotate
        elif direction == "R":
            dial += numberToRotate

        dial = NormalizeNumber(dial)
        
        if dial == 0:
            zeroCounter += 1
            
    return zeroCounter 

if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        result = GetResult(file)
        print(f"Answer: {result}")