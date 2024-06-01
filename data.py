from Shop import Shop
from CustomList import CustomList
import json


class Data:
    def __init__(self):
        self.data_list = CustomList()
        obj = Shop("Test", 10000)
        self.data_list.append(obj)

    def save_data(self):
        with open('data.json', 'w') as file:
            json.dump([obj.to_dict() for obj in self.data_list], file)

    def load_data(self):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                self.data_list = CustomList()
                for item in data:
                    obj = Shop(item['name'], item['overall_sold'])
                    self.data_list.append(obj)
        except FileNotFoundError:
            print("Error loading data from file")
