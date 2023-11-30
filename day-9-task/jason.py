import json

python_dict = {"name": "Jane", "age": 30, "isStudent": True, "grades": [88, 95, 87]}

class ToFromJson:
    def to(self, dic):
        return json.dumps(dic)
        

    def back_to(self, data):
        return json.loads(data)

j = ToFromJson().to(python_dict)
print(type(j))
d = ToFromJson().back_to(j)
print(type(d))
