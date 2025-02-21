print("Please write german or english words and we will translate them")
print("If you want to stop then write -> STOP")

t = True
while t:
    n = input()

    if n == "STOP":
        t = False

    else:
        c = 0
        f = open("dict.txt", "r")
        z = f.readline()
        for i in range(0, int(z)):
            x = f.readline()
            if n in x:
                print(x)
            else:
                c += 1
            if c == int(z):
                print("NOT FOUND", end = '\n')
        f.close()
        f1 = open("history.txt", "a")
        f1.write(n + "\n")
        f1.close()