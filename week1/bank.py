greeting = input("What is your greeting going to be?").strip().lower()

if greeting.startswith('hello') == True:
    print("$0")
elif greeting.startswith('h') == True and greeting.startswith('hello') == False:
    print("$20")
else:
    print("$100")
