def printing(msg):
    word=""
    i=0
    j=len(msg)-1
    while i<len(msg):
        if msg[j-i]==" ":
            print(word)
            word=""
        else:
            word=msg[j-i]+word
        i=i+1
    print(word)

printing("hello my friends where are you")