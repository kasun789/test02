BS = {}

def badCharactor(p):
    keys = []
    values = []
    l= len(p)
    i = 0
    for x in p:
        if(x not in keys and i != l-1):
            keys.append(x)
            values.append(l-1-i)
        elif (x not in keys and i == l-1):
            keys.append(x)
            values.append(l-1)
        elif(x in keys and i != l-1):
            m=0
            for y in keys:
                if(x == y):
                    values[m]= l-(i+1)
                m=m+1
        i=i+1
    for keys,values in zip(keys,values):
        BS[keys] = values

# '*' use to denote other characters in the patten
    
    BS.update({'*':l})
 


def MatchingString(txt,ptn):
    global matching_count
    m = len(txt)
    n = len(ptn)
    i = n-1
    j = n-1
    count = 0
    pos = 0
    prepos = 0

    while(j<m):
        i = n-1
        count = 0
        temp = j
        while(txt[j] == ptn[i]):
            j=j-1
            i=i-1
            count = count+1
        c = txt[pos + n-1]
        prepos=pos
        if c in BS:
            pos =pos + BS[c]
        else:
            pos =pos + BS["*"]
        j=temp+(pos-prepos)
        if(count==n):
            print(txt)
            matching_count=matching_count+1

with open("modules.txt") as f:
    text = f.readlines()
text = [x.strip() for x in text]
matching_count = 0
patten = input("Enter a search String : ")
badCharactor(patten)
for x in text:
    MatchingString(x,patten)

##for case-insensitive cases

newPatten = ""
if(patten[0].isupper()):
    newPatten +=patten[0].lower()
elif(patten[0].islower()):
    newPatten +=patten[0].upper()
for x in range (1,len(patten)):
    newPatten +=patten[x]
badCharactor(newPatten)
for x in text:
    MatchingString(x,newPatten)
print("Number of Macthes : ",matching_count)