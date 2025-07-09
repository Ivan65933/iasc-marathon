# завдання 1

students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]
mylist=[]
mylist1=[]
n=0
k=0

for i in range(len(grades)):
    s=grades[i]
    if n < s : 
        n=s
        k=i
    if s > 60 : mylist.append(students[i])
    if s < 60 : mylist1.append(students[i])

print(students[k])
print(mylist)
print(mylist1)

# завдання 2

logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
print(logs.count("ok"), logs.count("error"), logs.count("fail"), logs.count("warning"))
print(logs.count("error")/len(logs) * 100,"%")

# завдання 3

expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]
t : list = []
mylist2 = []
mylist3 = []
n = 100
k = 0
c = 0

for element in expenses:
    for el in element:
        if type(el) == int:
            mylist2.append(el)
for element in expenses:
    for el in element:
        if type(el) == str:
            mylist3.append(el)
for i in range(len(mylist2)):
    s = mylist2[i]
    if n < s:
        n = s
        k = i
    if s > 100: t.append(mylist3[i])
for i in range(len(mylist2)):
    c = c + mylist2[i]

print(mylist3[k])
print(c)
print(t)

# завдання 4

products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]
list1 = [item[0] for item in products]
list2 = [item[1] for item in products]
list3 = [item[2] for item in products]
list4 = [(item[1] * item[2]) for item in products]
n = 0
k = 0
pes = list(zip(list1, list4))

for i in range(len(list3)):
    s = list3[i]
    if n < s:
        n = s
for i in range(len(list4)):
    k = k + list4[i]

print(k)
print(n)        
print(pes)

# завдання 5

numbers = [10, 14, 18]
number = [x**2 for x in range(1, 31) if x % 2 == 0 and x % 4 != 0 and x not in numbers]
print(number)