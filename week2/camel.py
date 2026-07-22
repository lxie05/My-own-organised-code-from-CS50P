
result = ""
string = input("Enter your camelCase")

for i in string:
    if i.isupper():
        i = i.lower()
        result += "_" + i
    else:
        result += i

print (result)

