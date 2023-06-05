import os
import sys

sys.path.append(
    os.path.dirname(os.path.abspath(__file__)).split("Python_Tutorial")[0]
    + "Python_Tutorial"
)

from Config.Config import path

import json
from Manager import Manager


class Company:
    lstManager = []

    @classmethod
    def readJson(cls):
        try:
            cls.lstManager = []
            with open(path + "Classes\data.json", "r") as file:
                data = json.load(file)
            cls.lstManager = [Manager.jsonToObject(i) for i in data]
            print("Complete")
        except Exception as ex:
            print(ex)

    @classmethod
    def writeJson(cls):
        try:
            with open(path + "Classes\data.json", "w") as file:
                json.dump([i.toJson() for i in cls.lstManager], file)
            print("Complete")
        except Exception as ex:
            print(ex)

    @classmethod
    def show(cls):
        for i in cls.lstManager:
            i.Show()
        print("Complete")

    @classmethod
    def addManager(cls):
        cls.lstManager.append(Manager())
        print("Complete")

    @classmethod
    def deleteAll(cls):
        cls.lstManager = []
        print("Complete")
