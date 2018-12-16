#Calendar First Prototype (Python 2.x)
#Adam Suleman

def main ():
    print ("Select Read (r), Append (a), or Write(w)")
    choice = input()
    if choice == "r":
        f= open("testfile.txt","r")
        contents =f.read()
        print (contents)
        f.close()
    if  choice == "a":
        f= open("testfile.txt","r")
        contents =f.read()
        print (contents)
        f.close()
        f= open("testfile.txt","a")
        print ("What do you want to add to the file?")
        append = input()
        appendfile = f.write(" " + str(append))
        f.close()
    if choice == "w":
        f= open("testfile.txt","w+")
        contents =f.read()
        print (contents)
        print ("What do you want to add to the file?")
        write = input()
        writefile = f.write(" " + str(write))
        f.close()

def restart_main():
    print ("Would you like to restart(y/n)")
    restart = input()
    if restart == "y":
        main()
        restart_main()
    else:
        raise SystemExit
main ()
restart_main()
