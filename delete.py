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
            print(f"{_id} -Nömrəli ID databaseden silindi")
            break
    with open("db.json", "w") as connect:
        json.dump(data, connect)
    if finder == False:
        print(f"{_id} -Nömrəli ID tapılmadi")
