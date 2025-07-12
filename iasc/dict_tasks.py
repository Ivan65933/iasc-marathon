# завдання 1

contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}
contacts["Taras"] = "063-000-11-22"
print(contacts)
del contacts["Ivan"]
print(contacts)
print(contacts.keys())
print(contacts.values())
print("Katya" in contacts)

# завдання 2

grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}
mylist = []
mylist1 = list(grades.keys())
mylist2 = list(grades.values())
n = 0
k = 0
c = 0
b = 0

for i in range(len(mylist2)):
    s = mylist2[i]
    if n < s:
        n = s
        k = i
    if s > 80: mylist.append(mylist1[i])
for i in range(len(mylist2)):
    c = c + mylist2[i]
    b = i

print(mylist1[k])
print(c / (b+1))
print(mylist)

# завдання 3

transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
balances = {}
mylist3 = [item[0] for item in transactions]
mylist4 = [item[1] for item in transactions]
mylist5 = []
n = 0
k = 0
for name, amount in transactions:
    if name in balances:
        balances[name] += amount
    else:
        balances[name] = amount
for i in range(len(mylist4)):
    s = mylist4[i]
    if n < s:
        n = s
        k = i
    if s < 0: mylist5.append(mylist3[i])

print(balances)    
print(mylist3[k])
print(mylist5)

# завдання 4

text = "hello world hello again hello world test world"

words = text.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

# завдання 5

student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}

import json
json_string = json.dumps(student)

print("JSON:", json_string)

student_dict = json.loads(json_string)
student_dict["courses"].append("history")

print("словник:", student_dict)