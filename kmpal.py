from matplotlib.pyplot import flag


text ="abcdef"
patten ="bef"
flag = False

for i in range(0,len(text)):
    m=i
    for j in range(0,len(patten)):
        if(text[m]==patten[j]):
            flag = True
            m=m+1
        else:
            flag = False
            break
    if(flag):
        print("text have the patten")
        break

if(flag == False):
    print("text haven't patten")
