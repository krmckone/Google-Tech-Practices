#Author: Kaleb Robert McKone


S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}


def findLongest(matchWord, inputList):
    
    matchList = [] 
    
    for word in inputList:
        result = ""
        n = 0
        index = 0
        while n < len(word) and index < len(matchWord):
        # Avoid running out of bounds
                if matchWord[index] == word[n]:
                    result = result + word[n]
                    n = n + 1
                    # Update the result builder and move on to the next letter
                    # in both words
                    index = index + 1
                else:
                    index = index + 1
                    # No match; move forward in the matcher string
        if result == word:
            matchList.append(result)
            # Matched a full word
    return matchList    
        
       


if __name__ == "__main__":
    y = findLongest(S,D)
