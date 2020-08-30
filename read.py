import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def getProductbyPrice():
    _price = int(input("Qiyməti daxil edin: "))
    for d in data['products']:
        if d['productPrice'] < _price:
            print(
                f"ID:{d['productId']} | Name:{d['productName']} | Price:{d['productPrice']} | Count:{d['productCount']} ")


def getProductbyName():
    _name = input("Axdardiginiz modeli daxil edin: ")
    finder = False
    for d in data['products']:
        if d['productName'] == _name:
            print(
                f"ID:{d['productId']} \nName:{d['productName']} \nPrice:{d['productPrice']} \nCount:{d['productCount']} ")
            finder = True
            break
    if finder == False:
        print(f"{_name} -axtarişina uygun nəticə tapılmadı")
