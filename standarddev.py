def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for l in X:
        tot += (l - mean)**2
    return (tot/len(X))**0.5
    
def coVar(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('NaN')

def stdDevStringLengths(L):
    myLengths = []
    for i in range(len(L)): 
        myLengths.append(len(L[i]))

    if not myLengths:
        return float('NaN')
        
    mean = sum(myLengths)/float(len(myLengths))
    tot = 0.0
    for l in myLengths:
        tot += (l - mean)**2
    return (tot/len(myLengths))**0.5


#sList = ['apples', 'oranges', 'kiwis', 'pineapples']
#print stdDevStringLengths(sList)
        
#nList1 = [10,4,12,15,20,5]
#print coVar(nList1)

x1 = [0,1,2,3,4,5,6,7,8]
print stdDev(x1)

x2 = [5,10,10,10,15]
print stdDev(x2)

x3 = [0,1,2,4,6,8]
print stdDev(x3)

x4 = [6,7,11,12,13,15]
print stdDev(x4)

x5 = [9,0,0,3,3,3,6,6]
print stdDev(x5)
