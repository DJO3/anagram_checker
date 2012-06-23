## Checks if two words are anagrams

def ana(search, target):
    L1 = []
    L2 = []
    if target == search:
        return 0
    for i in target:
        L1.append(i)
    for j in search:
        L2.append(j)
    L1.sort(), L2.sort()
    if L1 == L2:
        return 1
    else:
        return 0

## For word in list, identifies number of anagrams of word within same list.
## Outputs as a dictionary.

def main(words):
    result = {}
    for word in words:
        num = 0
        pos = 0
        while pos+1 <= len(words):
            num = num + ana(words[pos],word)
            pos = pos + 1
            result[word] = num
    return result

list1 = ['bat','dog','god','bat','cat','tab','ogd','good','dogg','tab']

print main(list1)

##search,target = 'dog', 'god'
##search2,target2 = 'cat', 'dog'
##search3,target3 = 'good', 'dogg'
##
##print ana(search, target) 
##print ana(search2, target2)
##print ana(search3,target3)
