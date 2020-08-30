import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def updateDataFromId():
    _id = int(input("ID Daxil edin: "))
    _name = input("Name daxil edin: ")
    _price = int(input("Price daxil edin: "))
    _count = int(input("Count daxil edin: "))

    for product in data['products']:
        if product['productId'] == _id:
            product['productName'] = _name
            product['productPrice'] = _price
            product['productCount'] = _count
    with open("db.json", "w") as connect:
        json.dump(data, connect)
        print(f"ID-si {_id} olan datanın məlumatları müvəffəqiyyətlə yeniləndi!")

