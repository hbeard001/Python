def wordcount(msg):
    i=0
    space=0
    while i<len(msg):
        if msg[i]==" ":
            space=space+1
        i=i+1 
    print("this sentance has ",space+1," words")   
wordcount(input("a sentance: "))