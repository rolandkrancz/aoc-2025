
def Solution_part1(inputFile):
    invalidIds = []
    with open(inputFile, "r") as file:
        lines = file.readlines()
        for line in lines:
            idRanges = line.split(",")

            for idRange in idRanges:
                ids = idRange.split("-")
                startId = int(ids[0])
                endId = int(ids[1])
                invalidIdsInRange = _getInvalidIdsInRange(startId, endId)
                invalidIds.extend(invalidIdsInRange)
    
    return sum(invalidIds)

def _getInvalidIdsInRange(startId, endId):
    invalidIds = []
    for id in range(startId, endId + 1):
        idString = str(id)
        strLength = len(idString)
        idString_firstHalf = idString[:strLength // 2]
        idString_secondHalf = idString[strLength // 2:]
        
        if idString_firstHalf == idString_secondHalf:
            invalidIds.append(id)
        
    return invalidIds

if __name__ == "__main__":
    result_part1 = Solution_part1("input.txt")
    print(f"Part 1 Result: {result_part1}")