
user=0
pair=0
while True:

    user=input("Enter a number or 'exit' for exit : ")
    if user.lower()=="exit":
        break
    try:
        nombre = int(user)
        if nombre %2 ==0:
            pair+=1
    except ValueError:
        print("Invalid Entry! Try Again:")
print(pair)






