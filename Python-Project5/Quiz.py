a = { 'id': 89, 'name': "John" }
print (a['id'])

a = { 'id': 89, 'name': "John" }
print (a.get('id'))

a = { 'id': 89, 'name': "John" }
print (a.get('age'))

a = { 'id': 89, 'name': "John" }
print (a.get('age', 0))

a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
print (a.get('projects'))

a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
print (a.get('projects')[3])

a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
print (a.get('friends')[-1].get("name"))

for i in range(0, 3):
    print(i, end=" ")

for i in range(1, 4):
     print(i, end=" ")

for i in [1, 2, 3, 4]:
     print(i, end=" ")
     
for i in [1, 3, 4, 2]:
     print(i, end=" ")
     
for i in ["Hello", "Holberton", "School", 98]:
     print(i, end=" ")