import os

userPath = "data/Users/{}".format("kvarcas91")
if not os.path.exists(userPath):
    print("user doesn't exist")
    #os.mkdir(userPath)
else:
    with open(userPath+"/userData.txt", "r") as myfile:
        line = myfile.readlines()
        #if len(line) == 0:
         #   break
        passLine = []
        for x in line:
            passLine.append(x.split(' ')[2])
        if passLine[2].strip() == "i_love_baconf":
            print("True")
        else:
            print("False")
        #print(line, end = "")
        #for i in range(len(passLine)):
          #  print(passLine[i].strip())
           
        #data = myfile.read()
       # if data=="password":
       #     print("Correct")
       # else:
       #     print("Incorrect")
       # myfile.close()

