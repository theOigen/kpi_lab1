import json


def get_file_data(file_name):
    json_file = open(file_name, "r")
    content = json_file.read()
    return json.loads(content)


result = get_file_data("data.json")

for i in result["contacts"]:
    print(i["name"])

