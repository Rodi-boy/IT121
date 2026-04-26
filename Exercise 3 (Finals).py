try:
    Username = input("Enter Your Username: ")
    Age = int(input("Enter Your Age: "))

except ValueError:
    print("Invalid Input! Enter only a NUMBER for your AGE!")
except ZeroDivisionError:
    print("Invalid Age Number!")

else:
    with open("users.txt", "a") as file:
        file.write(f"{Username} - {Age}")
    
with open("users.txt", "r") as file:
    print(file.read())

print("System complete.")