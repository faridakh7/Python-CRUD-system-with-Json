import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")

def delProductbyName():
    _id = int(input("ID daxil edin: "))
    finder = False
    for product in data['products']:
        if product['productId'] == _id:
            data['products'].pop(data['products'].index(product))
            finder = True
            break
    with open("db.json", "w") as connect:
        json.dump(data,connect)
        print(f"{_id} -Nomreli ID databaseden silindi")
    if finder == False:
        print(f"{_id} -Nomreli ID tapilmadi")


