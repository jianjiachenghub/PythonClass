import csv
import json
io = open('pythonCSV.CSV')
json1 = csv.DictReader(io)
print(json1)
for i in list(json1):
    print(dict(i))

out = json.dumps( [ row for row in json1 ])
print(out)
# import Dataset
# imported_data = Dataset().load(open('/Users/br/Desktop/first100lines.csv').read())
# # export as json
# # (http://docs.python-tablib.org/en/latest/tutorial/#exporting-data)
# imported_data.json
# print(imported_data)