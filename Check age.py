age = int(input("Enter your age"))
def check_age(age):
    try: 
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age%2 == 0:
            print("Age is even")
        else:
            print("Age is odd")
    except ValueError:
        print("Age is invalid")

check_age(age)