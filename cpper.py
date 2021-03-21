a = ""
while True:
    try:
        a = input("")
    except EOFError:
        print("eof")
        break
    print(a)