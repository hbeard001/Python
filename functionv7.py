def printing(msg):
    word=""
    i=0
    while i<len(msg):
        if msg[len(msg)-i]==" ":
            print(word)
            word=""
        else:
            word=word+msg[i]
        i=i+1
    print(word)

printing("hello my friends where are you")