def printing2(msg):
    word=""
    i=len(msg)-1
    while i>=0:
        if msg[i]==" ":
            print(word)
            word=""
        else:
            word=msg[i]+word
        i=i-1
    print(word)

printing2("hello my friends where are you")