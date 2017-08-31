'''
Created on Aug 31, 2017

@author: jlearx
'''

def GetList():
    numlist = []
    
    while (len(numlist) == 0):
        listIn = input("Please enter a list of numbers inside []: ")
        start = listIn.find("[")
        finish = listIn.find("]")
        
        if ((start >= 0) and (finish > 0) and (finish != start + 1)):
            listIn = listIn[start + 1:finish]
            listIn = listIn.replace(" ", "")
            listStr = listIn.split(",")
            
            for s in listStr:
                numlist.append(int(s))
                
            break
        
    return numlist

def SlowSearch(numlist, number):
    found = False
    
    # Search checks each element until it finds the number,
    # from beginning to end
    # Potentially searches each element in the list
    
    for i in numlist:
        if (i == number):
            found = True
        
        if (found):
            break
    
    return found
    
def BinarySearch(numlist, number):    
    # List is assumed to be sorted numerically, 
    # so the search takes advantage of this fact

    return BinSearchRec(numlist, number)
        
def BinSearchRec(numlist, number):
    print(numlist)
    length = len(numlist)
    
    # Base case
    # If the list is empty, we reached end of the branch
    if (length == 0):
        return False
    
    # Choose the middle of the (sub)list as our guess
    midIdx = length / 2
    print(midIdx)
    middle = numlist[midIdx]
    
    # Did we find the number with our guess?
    if (middle == number):
        return True
    elif (middle < number):
        # The number is larger than our guess
        # Look on the right of our guess
        return BinSearchRec(numlist[midIdx + 1:], number)
    else:
        # The number is smaller than our guess
        # Look on the left of our guess        
        return BinSearchRec(numlist[:midIdx], number)

if __name__ == '__main__':
    numlist = GetList()
    number = int(input("Please enter the number to search for: "))
    
    print("Using slow search...")
    found = SlowSearch(numlist, number)
    
    if (found):
        print(str(True) + " - The number is in the list.")
    else:
        print(str(False) + " - The number is not in the list.")
        
    print("Using binary search...")
    found = BinarySearch(numlist, number)
    
    if (found):
        print(str(True) + " - The number is in the list.")
    else:
        print(str(False) + " - The number is not in the list.")        