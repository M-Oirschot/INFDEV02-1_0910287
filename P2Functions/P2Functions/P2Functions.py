class Empty:
    def __init__ (self):
        self.isEmpty = True
Empty = Empty()

class Node:
    def __init__ (self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail

userInput = int(input("How long must the list be?"))

l = Empty

for i in range(0, userInput):
    test = i + 1
    #print(i)
    l = Node(i,l)
x=l
 
def legacysum(x):
    Total = 0
    while not (x.isEmpty):
        Total += x.Value
        x = x.Tail
    return(Total)

def sum(x):
    if x.isEmpty:
        return 0
    else:
        return sum(x.Tail) + x.Value

def add(incrby, x):
    newlist = Empty
    if x.isEmpty:
        return 0
    else:
        x.Value = x.Value + incrby
        add(incrby, x.Tail)
        newlist = Node(x.Value, x.Tail)
        return newlist        

#do this assignment below with creating a new list
def filterEven(x):
    newlist = Empty
    if x.isEmpty:
        return 0
    else:
        if x.Value % 2 != 1:
            filterEven(x.Tail)
            newlist = Node(x.Value, x.Tail)
            return newlist
        else:
            return 0


#test = add(10, x)
test = filterEven(x)

while not(test.isEmpty):
    print test.Value
    test = test.Tail


#print(sum(x))
#print filterEven(x)