uniquewords=[]
def findunique(word):
    for w in uniquewords:
        if w==word:
            return False
    uniquewords.append(word)
    return True

def removedduplicates(msg):
    newmsg=""
    word=""
    i=0
    while i<len(msg):
        if msg[i]==" ":
            if findunique(word):
                newmsg=newmsg+word+" "
            word=""
        else:
            word=word+msg[i]
        i=i+1
    if findunique(word):
        newmsg=newmsg+word
    print(newmsg)
removedduplicates("hello hi hello hi shafeeq shafeeq hi")