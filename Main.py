from Tools import addTools


class Main:
    name = ["ToolName1", "ToolName2", "ToolName3"]
    quantity = [3, 3, 3]
    price = [1, 2, 3]
    description = ["Where's Stefan 1", "Tool description 2", "Tools description 3"]
    objList = []

    for i in range(3):
        object = addTools(name[i], quantity[i], price[i], description[i])
        objList.append(object)

    for i in range(len(objList)):
        print("Name:", objList[i].getName ())
        print("Quantity:", str(objList[i].getQuantity()))
        print("Price:", str(objList[i].getPrice()))
        print("Description:", (objList[i].getDescription()))
        print("-------------")
