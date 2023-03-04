# Opening file and reading

def file():

    myFile1 = open("file1.txt", "w")

    print("File name : ", myFile1.name)

    print("Opening mode : ", myFile1.mode)

    print("Closed or not : ", myFile1.close)

    myFile1 = open("file1.txt", "r")
    print(myFile1.read())

    myFile1 = open("file1.txt", "r")
    print(myFile1.read(5))

    myFile1 = open("file1.txt", "r")
    print(myFile1.readline())

    myFile1 = open("file1.txt", "r")
    print(myFile1.readline(20))

    myFile1 = open("file1.txt", "r")
    print(myFile1.readlines())

    myFile1 = open("file1.txt", "r")
    line1 = myFile1.readline()
    while line1:
        print(line1)
        line1 = myFile1.readline()
    myFile1.close()

    myFile1 = open("file1.txt", "r")
    for line2 in iter(myFile1):
        print(line2)
    myFile1.close()

    with open("file1.txt",  "r") as t_files:
        for line3 in t_files:
            print(line3)

    myFile1 = open("file1.txt", "w")
    myFile1.write("Test for write")
    myFile1.close()

    myFile2 = open("file2.txt", "w")
    myFile2.write("Hello World!")
    myFile2.close()

    myFile1 = open("file1.txt", "w")
    nameList = ["John\n", "Joe\n", "Jane\n"]
    myFile1.writelines(nameList)
    myFile1.close()

    myFile1 = open("file1.txt", "r")
    print(myFile1.read())

    myFile1.close()

file()
