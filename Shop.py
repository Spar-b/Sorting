import json


class Shop:
    def __init__(self, name, overall_sold):
        self.name = name
        self.overall_sold = overall_sold

    def to_dict(self):
        return {
            'name': self.name,
            'overall_sold': self.overall_sold
        }
