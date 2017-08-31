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
    
    for i in numlist:
        if (i == number):
            found = True
    
    return found
    
    

if __name__ == '__main__':
    numlist = GetList()
    number = int(input("Please enter the number to search for: "))
    found = SlowSearch(numlist, number)
    
    if (found):
        print(True + " - The number is in the list.")
    else:
        print(False + " - The number is not in the list.")