import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def showAllData():
    for d in data['products']:
        print(f"ID:{d['productId']} | Name:{d['productName']} | Price:{d['productPrice']} | Count:{d['productCount']} ")
