import json
import csv
arr = []
with open('test2.csv', 'r') as f:
    f_csv = csv.DictReader(f)
    for i in f_csv:
        print(dict(i))
        arr.append(i)
with open('test.json','w') as f:
    json.dump(arr,f,indent=4)
