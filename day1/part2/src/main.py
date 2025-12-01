import re

def GetResult(input):
    dial = 50
    zeroCounter = 0

    for line in input:
        direction = line[0]
        numberToRotate = int(re.findall(r'\d+', line)[0])
        
        isTurnedFromZero = (dial == 0)
        if direction == "L":
            dial -= numberToRotate
        elif direction == "R":
            dial += numberToRotate

        # Normalize dial and count zeroes
        if dial == 0:
            zeroCounter += 1
        else:
            while dial > 99:
                dial -= 100
                zeroCounter += 1
            while dial < 0:
                dial += 100
                if not isTurnedFromZero:
                    zeroCounter += 1
                else:
                    isTurnedFromZero = False
                if dial == 0:
                    zeroCounter += 1
            
    return zeroCounter 

if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        result = GetResult(file)
        print(f"Answer: {result}")