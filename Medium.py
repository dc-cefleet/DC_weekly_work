# find the smallest number

def smallnum(listofnums):
    return min(listofnums)
print(smallnum([9,3,5,2,1,5,12]))

def largenum(listofnums):
    return max(listofnums)
print(largenum([9,3,5,2,1,5,12]))

def longstring(listofstrings):
    largest = float('-inf')
    for string in listofstrings:
        if len(string) > largest:
            bigString = string
            largest = len(bigString)
    return bigString
print(longstring(["house", "water", "wolf", "brick", "mortar", "red", "coffee"]))

def shortstring(listofstrings):
    smallest = float('inf')
    for string in listofstrings:
        if len(string) < smallest:
            littleString = string
            smallest = len(littleString)
    return littleString
print(shortstring(["house", "water", "wolf", "brick", "mortar", "red", "coffee"]))
