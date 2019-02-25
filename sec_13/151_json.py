import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print('#############################')
a = json.dumps(j)
json.loads(a)
print(a)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(j, f)

print('#############################')
with open('test.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
