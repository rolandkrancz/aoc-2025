
def GetInvalidIds(startId, endId):
    return -1

def Solution_part1(inputFile):
    with open(inputFile, "r") as file:
        lines = file.readlines()
        for line in lines:
            idRanges = line.split(",")

            for idRange in idRanges:
                ids = idRange.split("-")
                startId = int(ids[0])
                endId = int(ids[1])
                invalidIds = GetInvalidIds(startId, endId)
                print(f"Invalid IDs for range {startId}-{endId}: {invalidIds}")
    return -1


if __name__ == "__main__":
    result_part1 = Solution_part1("input.txt")
    print(f"Part 1 result: {result_part1}")