#  To check if there are exactly 3 characters between 'a'/'A' and 'b'/'B' or vice versa. 

def abcheck(txt):
    txt = txt.casefold()
    for i in range(len(txt)):
        if txt[i] == 'a' and txt[i+4] == 'b':
            return True
        elif txt[i] == 'b' and txt[i+4] == 'a':
            return True
    print('not found')   



# To count the number of x's and o's in a string:

def xo(txt):
    xcount=0
    ocount=0
    for i in txt:
        if i .lower()== 'x':
            xcount += 1
        elif i.lower()== 'o':
            ocount += 1
    print('xcount is {}\nocount is {}'.format(xcount,ocount))




# Function to find if the given list of numbers follows arithmetic or geometric progression.

def arithgeo(arr):
    arr = np.array(arr)
    arith = True
    geo = True
    for i in range(1,len(arr)):
        a = arr[1]-arr[0]
        if arr[i]-arr[i-1] != a:
            arith = False
        b = arr[1]/arr[0]
        if i < len(arr):
            if arr[i-1]*b != arr[i]:
                geo = False
    return 'Arithmetic' if arith else 'Geometric' if geo else -1            




#  Get the middle 3 characters from a string


def get_middle_3_chars(x):
    l = len(x)
    ml = int(l/2)
    if l % 2 != 0 and l != 1 and l > 3:
        print("Middle 3 characters are : {}".format(x[ml-1:ml+2]))   
    else:
        print('Please give odd number of characters')



#  Remove duplicates from a list 

def removedup(l1):
    c = []
    for i in l1:
        if i not in c:
            c.append(i)
    return c

# OR there is always a simpler way:

def remove(x):
    return list(set(x))




# Find a to the power b using Recursion:


def power(num1,num2):
    if num2 == 1:
        return num1
    else:
        return num1*power(num1,num2-1)


# List comprehension 

# To count number of spaces in a string:-

string = 'There is a kite flying in the sky'
print( len( [i for i in string if i == ' '] ) )



# To get a list of all the consonants in a string

print([x for x in string if x not in ('a','e','i','o','u',' ') ] )



# To get the index and values from any iterable in the form of list of tuples 

x = ['Hello', 'Hi', 34 , 56.78,  100, 98,  (1,2,3) ]

print([(index,value) for index, value in enumerate(x)])



# Print all the common elements in 2 lists using list comprehension:

list1 = [1,2,3,4]
list2 = [3,4,5,6]

print( [ x for x in list1 if x in list2 ] )




# Print only the numbers from a string

str1= '1984 there were 13 instances of a protest with over 1000 people attending'

print([x for x in str1.split() if x.isnumeric()])






