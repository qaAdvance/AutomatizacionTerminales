import json


class Complementary:

    def __init__(self):
        self.directory = "string"
        self.input = "string"

    @staticmethod
    def read_json(directory):
        a = open(directory, "r")
        b = a.read()
        output = json.loads(b)
        return output

    @staticmethod
    def clean_quotation_marks(input):
        output = str(input).replace("\"", "\'")
        return output
