import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def addNewData():
    id = int(input("ID daxil edin: "))
    name = input("Ad daxil edin: ")
    price = int(input("Qiymet daxil edin: "))
    count = int(input("Say daxil edin: "))

    product = {
        "productId": id,
        "productName": name,
        "productPrice": price,
        "productCount": count
    }
    data['products'].append(product)
    with open("db.json", "w") as connect:
        json.dump(data, connect)
        print("Qeyd etdiyiniz parametrlər databaseyə daxil əlavə olundu!")
